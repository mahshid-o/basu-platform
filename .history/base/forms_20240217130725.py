from django.forms import ModelForm
from .models import Room , User
from django.contrib.auth.forms import UserCreationForm


class My(models.Model):
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 



class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields='__all__'
        exclude = ['host' , 'participants']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar' ,'name' ,'username' , 'email' , 'bio']


