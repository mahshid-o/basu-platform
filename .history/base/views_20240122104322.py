from django.shortcuts import render
from django.http import HttpResponse
# from django.http import HttpResponse

rooms = [
    {'id':1 , 'name':'lets learn python'}
    {'id':1 , 'name':'Design with me'}
    {'id':1 , 'name':'Frontend developers'}
]



def home(request):
    return render(request , 'home.html')

def room(request):
    return render(request , 'room.html')

