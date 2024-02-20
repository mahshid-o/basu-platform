from django.forms import ModelForm
from .models import Room , U


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields='__all__'
        exclude = ['host' , 'participants']
        
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username' , 'email']

