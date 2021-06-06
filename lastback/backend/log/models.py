from django.db import models
from user.models import User


# Create your models here.
class log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pic = models.ImageField(blank=True, null=True)
    log_date = models.DateTimeField(auto_now=True)
    danger = models.IntegerField(blank=True)
    category = models.IntegerField(blank=True)

