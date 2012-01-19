from datetime import datetime

from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    album = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(default=datetime.now)
    modified_date = models.DateTimeField(default=datetime.now)
