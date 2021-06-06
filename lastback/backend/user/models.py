from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50, blank=True)
    Email = models.CharField(max_length=200, blank=True)
    Ip = models.CharField(max_length=100, blank=True)
    makeDate = models.DateTimeField(auto_now=True)
