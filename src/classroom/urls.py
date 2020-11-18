from django.urls import path 
from . import views

app_name = 'classroom'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_classroom, name = 'create_classroom'),
    path('join/', views.join_classroom, name = 'join_classroom'),
    path('<int:pk>/', views.open_classroom, name = 'open_classroom'),
    path('<int:pk>', views.delete_classroom, name = 'delete_classroom'),
    path('<int:pk>/members', views.members, name = 'members_classroom'),

]