from django.shortcuts import render, redirect
from .models import Classroom
from .forms import ClassroomCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


def home(requests):
    classrooms = requests.user.classroom_set.all()
    classroom_form = ClassroomCreationForm()
    # print(classrooms)
    context = {
        'classrooms' : classrooms,
        'classroom_form': classroom_form,
    }
    return render(requests, 'classroom/home.html', context)

def create_classroom(request):
    print('IN CREATE_CLASSROOM')
    if request.method == 'POST':
        print('fORM vaLID')
        form = ClassroomCreationForm(request.POST)
        if form.is_valid(): 
            print(form.cleaned_data)
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            classroom = Classroom.objects.create(name=name, description=description, created_by=request.user)
            classroom.save()
            classroom.classroom_code = classroom.name[:4] + str(classroom.id)
            classroom.save()
            messages.success(request, f'Classroom {name} created !')
        else:
            messages.danger(request, f'Classroom Could not be created :(')

    return redirect('classroom:home')

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



