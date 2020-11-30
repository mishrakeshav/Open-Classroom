from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Course, FavouriteCourse
from .forms import CourseCreationForm, CourseUpdateForm


def course_list(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'courses/course_list.html', context)

@login_required
def create_course(request):
    if request.method == 'POST':
        form = CourseCreationForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course(
                title=form.cleaned_data.get('title'),
                description=form.cleaned_data.get('description'),
                link=form.cleaned_data.get('link'),
                image=form.cleaned_data.get('image'),
                created_by = request.user
            )
            course.save()
            return redirect('courses:course_list')
    else:
        form = CourseCreationForm()
    context={'form': form}
    return render(request, 'courses/create_course.html', context)

@login_required
def update_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method=='POST':
        form = CourseUpdateForm(request.POST,request.FILES,instance=course)
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

@login_required
def delete_course(request, pk):
    if request.method=='POST':
        course = get_object_or_404(Course, pk=pk)
        course.delete()
        messages.success(request, 'Course Deleted Successfully !')
        return redirect('courses:course_list')