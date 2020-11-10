from django.shortcuts import render
from .models import Classroom
from django.contrib.auth.models import User


def home(requests):
    classrooms = requests.user.classroom_set.all()
    print(classrooms)
    context = {
        'classrooms' : classrooms,
    }
    return render(requests, 'classroom/home.html', context)

def create_classroom(requests):
    context = {
        'title' : 'Classroom',
    }
    return render(requests, 'base.html', context)

def join_classroom(requests):
    context = {
        'title' : 'Classroom',
    }
    return render(requests, 'base.html', context)

def open_classroom(requests):
    context = {
        'title' : 'Classroom',
    }
    return render(requests, 'base.html', context)

def delete_classroom(requests):
    context = {
        'title' : 'Classroom',
    }
    return render(requests, 'base.html', context)



