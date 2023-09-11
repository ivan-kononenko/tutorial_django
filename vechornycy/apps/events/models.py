from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=24)
    publication_date = models.DateTimeField("Publication Date", auto_now_add=True)
    pic = models.ImageField(upload_to='media/', null=True, blank=True)
    event_body = models.TextField()
    date_event = models.DateTimeField("Date of an event")

    def __str__(self):
        return self.title


