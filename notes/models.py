from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    datetime = models.DateTimeField()
