from django.urls import path 
from . import views

app_name = 'assignments'

urlpatterns = [
    path('<int:pk>/view-grades/', views.view_grades, name='view_grades'),
    path('<int:pk>/grade/', views.grade, name='grade'),
]