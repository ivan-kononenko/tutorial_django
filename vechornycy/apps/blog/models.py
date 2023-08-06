from django.db import models
from mdeditor.fields import MDTextField


class Post(models.Model):
    title = models.CharField(max_length=24)
    publication_date = models.DateTimeField("Publication Date")
    post_body = models.TextField()

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=24)
    publication_date = models.DateTimeField("Publication Date")
    event_body = models.TextField()
    date_event = models.DateTimeField("Date of an event")

    def __str__(self):
        return self.title

