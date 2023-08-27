from django.contrib import admin

from .models import Post, Event


class PostAdmin(admin.ModelAdmin):
    list_display=('title', 'publication_date')

class EventAdmin(admin.ModelAdmin):
    list_display=('title', 'publication_date', 'date_event')

admin.site.register(Post, PostAdmin)
admin.site.register(Event, EventAdmin)
