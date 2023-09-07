from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=24)
    publication_date = models.DateTimeField("Publication Date")
    post_body = models.TextField()

    def __str__(self):
        return self.title

