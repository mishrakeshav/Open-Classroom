from django.urls import path 
from . import views

app_name = 'courses'

urlpatterns = [
    path('course_list', views.course_list, name='course_list'),
    path('create_course', views.create_course, name='create_course')
]