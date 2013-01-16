from django.db import models

class Animal(models.Model):
    rating = models.IntegerField(default=1000)
    link = models.URLField()