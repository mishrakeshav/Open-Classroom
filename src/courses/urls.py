from django.urls import path 
from . import views

app_name = 'courses'

urlpatterns = [
    path('course-list', views.course_list, name='course_list'),
    path('create-course', views.create_course, name='create_course'),
    path('update-course/<int:pk>', views.update_course, name='update_course'),
    path('delete-course/<int:pk>', views.delete_course, name='delete_course'),
]