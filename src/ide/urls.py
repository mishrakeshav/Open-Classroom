from django.urls import path 
from . import views

app_name = 'ide'

urlpatterns = [
    path('', views.ide, name="ide"),
    path('problems/', views.problems, name="problems"),
]