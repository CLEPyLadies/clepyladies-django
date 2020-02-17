import uuid

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    event_name = models.CharField(max_length=200)
    event_description = models.TextField()

    def publish(self):
        self.save()

    def __str__(self):
        return self.event_name

class EventInstance(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    event_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("event-detail", kwargs={"id": self.id})
    

    def __str__(self):
        return f'{self.event_date}: {self.event.__str__()}'


class CheckIn(models.Model):
    attendee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event = models.ForeignKey(EventInstance, on_delete=models.CASCADE)
    checkin_date = models.DateTimeField(default=timezone.now)

    ATTENDEE_STATUS = (
        ('o','Organizer'),
        ('f','First Timer'),
        ('r','Repeat Attendee'),
    )

    attendee_type = models.CharField(
        max_length=1,
        choices=ATTENDEE_STATUS,
        blank=True,
        default='f',
        help_text='Attendee type',
    )

    def update(self):
        self.checkin_date = timezone.now()
        self.save()

    def __str__(self):
        return self.event.__str__()

# per https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=200, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    github_username = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.user.last_name}, {self.user.first_name}'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()