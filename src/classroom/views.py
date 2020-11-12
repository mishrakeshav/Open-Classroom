from django.shortcuts import render, redirect
from .models import Classroom
from .forms import ClassroomCreationForm,JoinClassroomForm
from django.contrib.auth.models import User
from django.contrib import messages


def home(requests):
    classrooms = requests.user.classroom_set.all()
    classroom_form = ClassroomCreationForm()
    join_classroom_form = JoinClassroomForm()
    context = {
        'classrooms' : classrooms,
        'classroom_form': classroom_form,
        'join_classroom_form':join_classroom_form
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

def join_classroom(request):
    print('IN CREATE_CLASSROOM')
    if request.method == 'POST':
        print('fORM vaLID')
        form = JoinClassroomForm(request.POST)
        if form.is_valid(): 
            classroom = Classroom.objects.filter(classroom_code = form.cleaned_data.get('code')).first()
            # print(classroom.users.create(request.user))
            request.user.classroom_set.add(classroom)
            messages.success(request, f'You are added in {classroom.name}')
        else:
            messages.danger(request, f'Error adding you to the classroom')
    return redirect('classroom:home')


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



