from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def whiteboard(request):
    context = {}
    return render(request, 'whiteboard/whiteboard.html', context)

@login_required
def live(request):
    context = {}
    return render(request, 'whiteboard/liveboard.html', context)
