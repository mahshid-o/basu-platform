from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponse

rooms = [
    {'id':}
]



def home(request):
    return render(request , 'home.html')

def room(request):
    return render(request , 'room.html')

