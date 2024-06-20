from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Item(models.Model):
    itemId = models.CharField(max_length =100)
    name = models.TextField(blank=False)
    person = models.ForeignKey(User, on_delete= models.CASCADE)

class Location(models.Model):
        locationId = models.CharField(max_length =100)
        location = models.TextField(blank=False)
        item = models.ForeignKey(Item, on_delete= models.CASCADE)
        
