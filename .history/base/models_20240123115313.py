from django.db import models

# Create your models here.

class Room(models.Model):
    #host =
    #topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True , blank = True) #it cant be blank (null=True)for database   blank=True save method in form  
    #participants = 
    updated = models.DateTimeField(auto_now=)