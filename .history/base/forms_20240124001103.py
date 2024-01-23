from django.forms import ModelForm
from .models import Room


class RoomForm(ModelForm):
    
    class class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
    

    def __str__(self):
        return 

