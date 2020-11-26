from django.urls import path,include
from . import views

app_name='comments'

urlpatterns = [
    path('comment/create/<int:post_pk>/', views.create_comment, name='create_comment'),
]