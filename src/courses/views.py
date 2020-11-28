from django.shortcuts import get_object_or_404, redirect, render
from .models import Course, FavouriteCourse
from .forms import CourseCreationForm, CourseUpdateForm
from django.contrib import messages

def course_list(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'courses/course_list.html', context)

def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('courses:course_list')
    else:
        form = CourseCreationForm()
    context={'form': form}
    return render(request, 'courses/create_course.html', context)

def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method=='POST':
        form = CourseUpdateForm(data=request.POST, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course Updated Successfully')
        else:
            messages.danger(request, 'Course Updated Failed')

        return redirect('courses:update_course', course.pk)
    else:
        form = CourseUpdateForm(instance=course)
    context = {'form': form, 'course':course}
    return render(request, 'courses/course_update.html', context)
