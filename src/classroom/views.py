from django.shortcuts import render


def home(requests):
    context = {
        'title' : 'Classroom',
    }
    return render( requests,'classroom/index.html', context)
