from django.urls import path
from . import views


urlpatterns = [
    path('', views.add_message, name='add_message'),
   
]