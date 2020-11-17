from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .models import Classroom,Topic
from .forms import ClassroomCreationForm,JoinClassroomForm, PostForm


@login_required
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

@login_required
def create_classroom(request):
    if request.method == 'POST':
        print('fORM vaLID')
        form = ClassroomCreationForm(request.POST)
        if form.is_valid(): 
            name = form.cleaned_data.get('name')
            description = form.cleaned_data.get('description')
            classroom = Classroom.objects.create(name=name, description=description, created_by=request.user)
            classroom.save()
            classroom.classroom_code = classroom.name[:4] + str(classroom.id)
            classroom.save()
            topic = Topic(name = 'General' , classroom = classroom)
            topic.save()
            messages.success(request, f'Classroom {name} created !')
        else:
            messages.danger(request, f'Classroom Could not be created :(')
    return redirect('classroom:home')

@login_required
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

@login_required
def open_classroom(requests,pk):
    classroom = get_object_or_404(Classroom,pk = pk)
    topics = classroom.topic_set.all()
    contents = []
    for topic in topics:
        contents.extend(list(topic.post_set.all()))
        contents.extend(list(topic.assignment_set.all()))
    
    contents.sort(key = lambda x: x.created_at)

    post_form = PostForm()

    context = {
        'title' : 'Classroom',
        'classroom' : classroom,
        'contents': contents,
        'post_form': post_form
    }

    return render(requests, 'classroom/classroom.html', context)

@login_required
def delete_classroom(requests):
    context = {
        'title' : 'Classroom',
    }
    return render(requests, 'base.html', context)

