from django import forms
from .models import Semester, Course, Class, Lecturer, Student, StudentEnrollment

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ['year', 'semester']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['code', 'name']

class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['number', 'semester', 'course', 'lecturer']

class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ['staffID', 'firstName', 'lastName', 'email', 'course', 'DOB']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['studentID', 'firstName', 'lastName', 'email', 'DOB']

class StudentEnrollmentForm(forms.ModelForm):
    class Meta:
        model = StudentEnrollment
        fields = ['student', 'class_obj', 'grade', 'enrol_time', 'grade_time']

class LoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
