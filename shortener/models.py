from django.db import models
from django.contrib.auth.models import User

class ShortUrlGuest(models.Model):
    shortUrl = models.CharField(max_length=100, unique=True)
    longUrl = models.CharField(max_length=100)

    def __str__(self):
        return self.shortUrl + "Guest"

class ShortUrlAuth(models.Model):
    shortUrl = models.CharField(max_length=100, unique=True)
    longUrl = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    timesClicked = models.IntegerField(default=0)

    def __str__(self):
        return self.shortUrl
