from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    
    class Meta:
        model = Room
        fields='__all'
    

    def __str__(self):
        return 

