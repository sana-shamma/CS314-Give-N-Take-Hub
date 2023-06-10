from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#customer table
class customer(models.Model):
    userID = models.AutoField(primary_key=True)
    userName = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(unique=True,blank=False, null=False)
    password = models.CharField( max_length=255,blank=False, null=False)
    points =  models.IntegerField(default=0)

    def __str__(self):
        return self.userName
    
