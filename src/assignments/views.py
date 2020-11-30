from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from posts.models import SubmittedAssignment,Assignment
from classroom.models import Classroom
from comments.forms import PrivateCommentForm
from .forms import GradeStudentForm

@login_required
def view_grades(request,pk):
    assignment = get_object_or_404(Assignment,pk=pk)
    submitted_assignments = assignment.submittedassignment_set.all()
    context = {
        'submitted_assignments':submitted_assignments,
        'assignment':assignment,
    }
    return render(request, 'assignments/view_grades.html', context)

@login_required
def grade(request,pk):
    submit_assignment = get_object_or_404(SubmittedAssignment, pk=pk)
    if request.method == 'POST':
        grade_form = GradeStudentForm(request.POST)
        if grade_form.is_valid():
            grade = grade_form.cleaned_data.get('grade')
            submit_assignment.is_reviewed = True
            submit_assignment.grade = grade 
            submit_assignment.save()
        else:
            print('not valid')
    else:
        grade_form = GradeStudentForm() 
            
    assignment_files = submit_assignment.assignmentfile_set.all()
    context = {
        'submit_assignment':submit_assignment,
        'assignment_files':assignment_files,
        'grade_form':grade_form,
    }
    return render(request, 'assignments/grade.html', context)