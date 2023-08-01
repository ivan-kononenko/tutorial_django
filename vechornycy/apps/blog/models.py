from django.db import models
from mdeditor.fields import MDTextField


class Post(models.Model):
    publication_date = models.DateTimeField("Publication Date")
    post_body = MDTextField(null=True, blank=True)


class Event(models.Model):
    publication_date = models.DateTimeField("Publication Date")
    event_body = MDTextField(null=True, blank=True)
    date_event = models.DateTimeField("Date of an event")

