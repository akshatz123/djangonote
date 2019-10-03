from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    """docstring for Profile"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
    	user  = self.user
    	return Profile.objects.filter(user=user)