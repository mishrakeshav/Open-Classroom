from django.urls import path 
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_classroom, name = 'create_classroom'),
]