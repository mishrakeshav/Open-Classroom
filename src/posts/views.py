from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Assignment, Post,Resource
from classroom.models import Classroom,Topic
from classroom.forms import PostForm


@login_required
def create_post(request, pk):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            classroom = get_object_or_404(Classroom,pk = pk)
            topic = classroom.topic_set.first()
            title = form.cleaned_data.get('title')
            description = form.cleaned_data.get('description')
            files = request.FILES.getlist('file_field')
            post = Post.objects.create(title=title,description=description,created_by=request.user, topic = topic)
            for f in files:
                Resource.objects.create(post = post,files=f)
            
            messages.success(request, f'Post Created {title}')
        else:
            messages.danger(request, f'Cannot create post')
    
    return redirect('classroom:open_classroom', pk)