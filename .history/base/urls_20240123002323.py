from django.urls import path
from . import views


urlpatterns = [
    path('',views.home , name="home"),
    path('room_/<str:pk>/',views.room , name="room")
]

