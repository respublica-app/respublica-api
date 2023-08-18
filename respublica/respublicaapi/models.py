from django.db import models

class Tools(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=255)
    logo = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    official = models.BooleanField()
    author = models.CharField(max_length=100)
    description = models.CharField(max_length=255)