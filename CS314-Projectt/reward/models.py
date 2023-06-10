from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username

class Coupon(models.Model):
    sponsor_name = models.CharField(max_length=200)
    expiration_date = models.DateField()
    needed_points = models.IntegerField()
    unique_code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.sponsor_name