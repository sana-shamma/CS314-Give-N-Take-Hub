from django.db import models

# Create your models here.
class sponsor(models.Model):
    name= models.CharField(max_length=250)
    logo = models.ImageField()
#The nama of the item will appear in front of administrator 
    def __str__(self):
        return self.name