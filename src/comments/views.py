from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentCreateForm
from .models import Comment
from posts.models import Post

@login_required
def create_comment(request, post_pk):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            post = get_object_or_404(Post, pk=post_pk)
            comment = Comment(
                user=request.user, 
                comment_text=form.cleaned_data.get('comment_text'),
                post = post
            )
            comment.save()
            return redirect('classroom:open_classroom', post.topic.classroom.pk)
