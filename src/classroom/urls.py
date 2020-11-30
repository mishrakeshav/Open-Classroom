from django.urls import path 
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_classroom, name = 'create_classroom'),
    path('join/', views.join_classroom, name = 'join_classroom'),
    path('open/<int:pk>/', views.open_classroom, name = 'open_classroom'),
    path('<int:pk>', views.delete_classroom, name = 'delete_classroom'),
    path('<int:pk>/members', views.members, name = 'members_classroom'),
    path('assignment/<int:pk>/student_work', views.student_work, name = 'student_work'),
    path('assignment/create', views.assignment_create, name = 'assignment_create'),
    path('assignment/<int:pk>', views.assignment_submit, name = 'assignment_submit'),
    path('assignment/<int:pk>/turnin/', views.turnin, name = 'turnin'),
    path('assignment/<int:pk>/unsubmit/', views.unsubmit, name = 'unsubmit'),
    path('assignment/<int:pk>/unsubmit_file/', views.unsubmit_file, name = 'unsubmit_file'),
    path('todo/', views.todo, name = 'todo'),
    path('toreview/', views.toreview, name = 'toreview'),
    path('<int:pk>/classwork/', views.classwork, name = 'classwork'),
]