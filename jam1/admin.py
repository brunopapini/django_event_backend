from django.contrib import admin

# Register your models here.

from .models import Event, Profile

admin.site.register(Event)
admin.site.register(Profile)