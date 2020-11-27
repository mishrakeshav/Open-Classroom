from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def whiteboard(request):
    context = {}
    return render(request, 'whiteboard/whiteboard.html', context)
