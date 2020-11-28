from django.shortcuts import render

# Create your views here.


def ide(request):
    context = {}
    return render(request, 'ide/ide.html', context)

def problems(request):
    context = {}
    return render(request, 'ide/problems.html', context)