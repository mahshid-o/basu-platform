from django.urls import path
from . import views


urlpatterns = [
    path('',views.home , name),
    path('room/',room)
]

