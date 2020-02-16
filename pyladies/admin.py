from django.contrib import admin

from pyladies.models import Attendance, Event, Profile

# Register your models here.
admin.site.register(Attendance)
admin.site.register(Event)
admin.site.register(Profile)