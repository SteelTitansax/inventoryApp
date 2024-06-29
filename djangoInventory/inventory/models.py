from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Location(models.Model):
        location = models.TextField(blank=False)

 
class Item(models.Model):
    name = models.TextField(blank=False)
    person = models.ForeignKey(User, on_delete= models.CASCADE)
    location = models.ForeignKey(Location, on_delete= models.CASCADE)
    comments = models.TextField(blank=True)
    date = models.DateField(default=datetime.datetime.now() )

    