from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('t', 'traveler'),
        ('a', 'agency'),
    )
    type = models.CharField(max_length =1, choices = USER_TYPES, null=True, blank=True)
    class Meta():
        db_table = 'user'

class Traveler(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    introduction = models.CharField(max_length=1000, null=True, blank=True)

class Agency(models.Model):
    user = models.OneToOneField(to=CustomUser, on_delete=models.CASCADE)
    location = models.CharField(max_length=200)



