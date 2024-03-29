from django.db import models
from django import forms

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length = 264)
    last_name = models.CharField(max_length = 264)
    email = models.CharField(max_length = 264, unique = True)

    def __str__(self):
        return self.first_name
