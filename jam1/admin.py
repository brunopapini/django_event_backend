from django.contrib import admin

# Register your models here.

from .models import Event, Profile, Intereses, Instrument

admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Intereses)
admin.site.register(Instrument)