from django.db import models

# Create your models here.

class Room(models.Model):
    #host =
    #topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True , blank = True) #it cant be blank (null=True)for database   blank=True save method in form  
    #participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name
    
class Message(models.Model):
    #user =
    room = models.ForeignKey(Room , on_delete=models.CASCADE)#when the room delete , 


    def __str__(self):
        return 

    def __unicode__(self):
        return 
