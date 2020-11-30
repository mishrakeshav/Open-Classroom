from django.urls import path 
from . import views

app_name = 'whiteboard'

urlpatterns = [
    path('', views.whiteboard, name='whiteboard'),
    path('liveboard/', views.liveboard, name='liveboard'),
]