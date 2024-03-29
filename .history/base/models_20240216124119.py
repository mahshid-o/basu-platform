from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

# class Topic(models.Model):
#     name = models.CharField(max_length=200)

#     def __str__(self):
#         return self.name



# class Room(models.Model):
#     host = models.ForeignKey(User , on_delete=models.SET_NULL , null=True)
#     topic = models.ForeignKey(Topic , on_delete=models.SET_NULL , null=True)
#     name = models.CharField(max_length=200)
#     description = models.TextField(null=True , blank = True) #it cant be blank (null=True)for database   blank=True save method in form  
#     participants = models.ManyToManyField(User,related_name='participants',blank=True)
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add = True)


#     class Meta:
#         ordering=['-updated','-created']

#     def __str__(self):
#         return self.name

# class Message(models.Model):
#     user = models.ForeignKey(User , on_delete= models.CASCADE) 
#     room = models.ForeignKey(Room , on_delete=models.CASCADE)#when the room delete ,all the messages delete too(all the children delete)
#     body = models.TextField()
#     updated = models.DateTimeField(auto_now=True)
#     created = models.DateTimeField(auto_now_add = True)

#     class Meta:
#         ordering=['-updated','-created']

#     def __str__(self):
#         return self.body[0:50]

#     def __unicode__(self):
#         return 
