from django.db import models

# Create your models here.

class Room(models.Model):
    #host =
    #topic = 
    name = models.charfield(max_length=200)
    description = models.TextField