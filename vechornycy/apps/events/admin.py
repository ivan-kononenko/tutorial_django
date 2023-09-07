from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display=('title', 'publication_date', 'date_event')

admin.site.register(Event, EventAdmin)

# Register your models here.
