from django.urls import path 
from . import views

app_name = 'whiteboard'

urlpatterns = [
    path('', views.whiteboard, name='whiteboard'),
    path('live/', views.live, name='live'),
]