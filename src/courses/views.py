from django.shortcuts import render, redirect
from .models import Course, FavouriteCourse
from .forms import CourseCreationForm

def course_list(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'courses/course_list.html', context)

def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('courses:course_list')
    else:
        form = CourseCreationForm()
    context={'form': form}
    return render(request, 'courses/create_course.html', context)