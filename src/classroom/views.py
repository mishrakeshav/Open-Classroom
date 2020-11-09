from django.shortcuts import render


def home(requests):
    context = {
        'title' : 'Classroom',
    }
    return render(requests, 'base.html', context)

