from django.db import models

class Post(models.Model):
    publication_date = models.DateTimeField("Publication Date")
    text = models.CharField(max_length=4000)

class Event(models.Model):
    publication_date = models.DateTimeField("Publication Date")
    text = models.Charfield(max_length=4000)
    date_event = models.DateTimeField("Date of an event")
