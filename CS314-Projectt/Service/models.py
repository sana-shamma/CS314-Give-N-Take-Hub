from django.db import models
# Create your models here.
# Database For Borrowed Item
class borrowedItem(models.Model):
    name= models.CharField(max_length=250)
    owner = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    description = models.TextField()
    image = models.ImageField()
#The nama of the item will appear in front of administrator 
    def __str__(self):
        return self.name
    
# Database For Swaped Item
class swapedItem(models.Model):
    name= models.CharField(max_length=250)
    owner = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    description = models.TextField()
    image = models.ImageField()

#The nama of the item will appear in front of administrator 
    def __str__(self):
        return self.name
    
# Database For Gift Item
class giftItem(models.Model):
    name= models.CharField(max_length=250)
    owner = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    description = models.TextField()
    image = models.ImageField()

#The nama of the item will appear in front of administrator 
    def __str__(self):
        return self.name

