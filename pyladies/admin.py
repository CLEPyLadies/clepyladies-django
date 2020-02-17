from django.contrib import admin

from pyladies.models import CheckIn, Event, EventInstance, Profile

# Register your models here.
admin.site.register(CheckIn)
admin.site.register(Event)
admin.site.register(EventInstance)
admin.site.register(Profile)