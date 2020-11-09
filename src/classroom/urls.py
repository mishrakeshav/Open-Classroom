from django.urls import path 
from . import views

app_name = 'classroom'

urlpatterns = [
    path('home/', views.home,name='home'),
]