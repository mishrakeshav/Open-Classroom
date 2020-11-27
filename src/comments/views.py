from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from .forms import CommentCreateForm, PrivateCommentForm
from .models import Comment, PrivateComment
from posts.models import Post, Assignment

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

@login_required
def create_private_comment(request, assignment_pk):
    if request.method == 'POST':
        form = PrivateCommentForm(request.POST)
        if form.is_valid():
            assignment = get_object_or_404(Assignment, pk=assignment_pk)
            comment = PrivateComment(
                user=request.user, 
                comment_text=form.cleaned_data.get('comment_text'),
                assignment = assignment
            )
            comment.save()
            return redirect('classroom:assignment_submit', assignment.pk)
