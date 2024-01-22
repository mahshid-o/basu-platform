from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponse

rooms = [
    {'id':1 , }
]



def home(request):
    return render(request , 'home.html')

def room(request):
    return render(request , 'room.html')

