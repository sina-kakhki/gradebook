from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.forms import forms

from gradebook.forms import SemesterForm, CourseForm, ClassForm, LecturerForm, StudentForm, StudentEnrollmentForm
from gradebook.models import *


# Administrator views
@login_required
def semester_list(request):
    semesters = Semester.objects.all()
    return render(request, 'semester_list.html', {'semesters': semesters})


@login_required
def semester_create(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()
    return render(request, 'semester_form.html', {'form': form})


@login_required
def semester_detail(request, pk):
    semester = Semester.objects.get(pk=pk)
    return render(request, 'semester_detail.html', {'semester': semester})


@login_required
def semester_update(request, pk):
    semester = Semester.objects.get(pk=pk)
    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm(instance=semester)
    return render(request, 'semester_form.html', {'form': form})


@login_required
def semester_delete(request, pk):
    semester = Semester.objects.get(pk=pk)
    semester.delete()
    return redirect('semester_list')


@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})


@login_required
def course_create(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'course_form.html', {'form': form})


@login_required
def course_detail(request, pk):
    course = Course.objects.get(pk=pk)
    return render(request, 'course_detail.html', {'course': course})


@login_required
def course_update(request, pk):
    course = Course.objects.get(pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'course_form.html', {'form': form})


@login_required
def course_delete(request, pk):
    course = Course.objects.get(pk=pk)
    course.delete()
    return redirect('course_list')


@login_required
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})


@login_required
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render(request, 'class_form.html', {'form': form})


@login_required
def class_detail(request, pk):
    class_obj = Class.objects.get(pk=pk)
    return render(request, 'class_detail.html', {'class': class_obj})


@login_required
def class_update(request, pk):
    class_obj = Class.objects.get(pk=pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=class_obj)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm(instance=class_obj)
    return render(request, 'class_form.html', {'form': form})


@login_required
def class_delete(request, pk):
    class_obj = Class.objects.get(pk=pk)
    class_obj.delete()
    return redirect('class_list')


@login_required
def lecturer_list(request):
    lecturers = Lecturer.objects.all()
    return render(request, 'lecturer_list.html', {'lecturers': lecturers})


@login_required
def lecturer_create(request):
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm()
    return render(request, 'lecturer_form.html', {'form': form})


@login_required
def lecturer_detail(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    return render(request, 'lecturer_detail.html', {'lecturer': lecturer})


@login_required
def lecturer_update(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    if request.method == 'POST':
        form = LecturerForm(request.POST, instance=lecturer)
        if form.is_valid():
            form.save()
            return redirect('lecturer_list')
    else:
        form = LecturerForm(instance=lecturer)
    return render(request, 'lecturer_form.html', {'form': form})


@login_required
def lecturer_delete(request, pk):
    lecturer = Lecturer.objects.get(pk=pk)
    lecturer.delete()
    return redirect('lecturer_list')


@login_required
def assign_lecturer(request, class_pk):
    class_obj = Class.objects.get(pk=class_pk)
    if request.method == 'POST':
        form = LecturerForm(request.POST)
        if form.is_valid():
            lecturer = form.cleaned_data['lecturer']
            class_obj.lecturer = lecturer
            class_obj.save()
            return redirect('class_list')
    else:
        form = LecturerForm()
    return render(request, 'assign_lecturer.html', {'form': form, 'class': class_obj})


@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})


@login_required
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_detail(request, pk):
    student = Student.objects.get(pk=pk)
    return render(request, 'student_detail.html', {'student': student})


@login_required
def student_update(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})


@login_required
def student_delete(request, pk):
    student = Student.objects.get(pk=pk)
    student.delete()
    return redirect('student_list')


@login_required
def enroll_student(request, class_pk):
    class_obj = Class.objects.get(pk=class_pk)
    if request.method == 'POST':
        form = StudentEnrollmentForm(request.POST)
        if form.is_valid():
            student = form.cleaned_data['student']
            grade = form.cleaned_data['grade']
            enrol_time = form.cleaned_data['enrol_time']
            grade_time = form.cleaned_data['grade_time']
            enrollment = StudentEnrollment(student=student, class_obj=class_obj, grade=grade,
                                           enrol_time=enrol_time, grade_time=grade_time)
            enrollment.save()
            return redirect('class_detail', pk=class_pk)
    else:
        form = StudentEnrollmentForm()
    return render(request, 'enroll_student.html', {'form': form, 'class': class_obj})


@login_required
def remove_student(request, enrollment_pk):
    enrollment = StudentEnrollment.objects.get(pk=enrollment_pk)
    class_pk = enrollment.class_obj.pk
    enrollment.delete()
    return redirect('class_detail', pk=class_pk)


@login_required
def student_enrollment_list(request, student_pk):
    student = Student.objects.get(pk=student_pk)
    enrollments = student.studentenrollment_set.all()
    return render(request, 'student_enrollment_list.html', {'student': student, 'enrollments': enrollments})


# Login and Logout views
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login


def login_lecturer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active and user.is_lecturer:
            login(request, user)
            return redirect('dashboard')  # Redirect to lecturer dashboard
        else:
            # Invalid credentials or user is not a lecturer
            error_message = 'Invalid login credentials'
    else:
        error_message = ''
    return render(request, 'login_lecturer.html', {'error_message': error_message})


def login_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_active and user.is_student:
            login(request, user)
            return redirect('dashboard')  # Redirect to student dashboard
        else:
            # Invalid credentials or user is not a student
            error_message = 'Invalid login credentials'
    else:
        error_message = ''
    return render(request, 'login_student.html', {'error_message': error_message})


def logout_view(request):
    logout(request)
    return redirect('index')


class AssignClassForm(forms.Form):
    lecturer = forms.ModelChoiceField(queryset=Lecturer.objects.all(), empty_label=None, label='Select Lecturer')


def assign_class(request, lecturer_id):
    lecturer = get_object_or_404(Lecturer, id=lecturer_id)
    if request.method == 'POST':
        form = AssignClassForm(request.POST)
        if form.is_valid():
            class_id = form.cleaned_data['class']
            class_obj = get_object_or_404(Class, id=class_id)
            lecturer.class_assigned = class_obj
            lecturer.save()
            return redirect('view_lecturer', pk=lecturer_id)
    else:
        form = AssignClassForm()

    context = {'form': form, 'lecturer': lecturer}
    return render(request, 'assign_class.html', context)


def index(request):
    if request.user.is_authenticated:
        # User is logged in
        context = {
            'user': request.user,
        }
    else:
        # User is not logged in
        context = {}

    return render(request, 'index.html', context)


def create_semester(request):
    if request.method == 'POST':
        form = SemesterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('semester_list')
    else:
        form = SemesterForm()

    context = {'form': form}
    return render(request, 'create_semester.html', context)


def view_semester(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)

    context = {'semester': semester}
    return render(request, 'view_semester.html', context)


def update_semester(request, semester_id):
    semester = get_object_or_404(Semester, id=semester_id)

    if request.method == 'POST':
        form = SemesterForm(request.POST, instance=semester)
        if form.is_valid():
            form.save()
            return redirect('view_semester', semester_id=semester_id)
    else:
        form = SemesterForm(instance=semester)

    context = {'form': form, 'semester': semester}
    return render(request, 'update_semester.html', context)
