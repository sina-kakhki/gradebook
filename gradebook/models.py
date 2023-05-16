from django.db import models


class Semester(models.Model):
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=50)

    @classmethod
    def create_semester(cls, year, semester):
        semester = cls(year=year, semester=semester)
        semester.save()
        return semester

    def update_semester(self, year, semester):
        self.year = year
        self.semester = semester
        self.save()
        return self

    def delete_semester(self):
        self.delete()

    @staticmethod
    def get_semester(semester_id):
        try:
            semester = Semester.objects.get(pk=semester_id)
            return semester
        except Semester.DoesNotExist:
            return None


class Course(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE, related_name='courses')

    @classmethod
    def create_course(cls, code, name):
        course = cls(code=code, name=name)
        course.save()
        return course

    def update_course(self, code, name):
        self.code = code
        self.name = name
        self.save()
        return self

    def delete_course(self):
        self.delete()

    @staticmethod
    def get_course(course_id):
        try:
            course = Course.objects.get(pk=course_id)
            return course
        except Course.DoesNotExist:
            return None


class Lecturer(models.Model):
    staffID = models.CharField(max_length=50)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    DOB = models.DateField()
    course = models.ManyToManyField(Course)

    def create_lecturer(self, staffID, firstName, lastName, email, DOB):
        lecturer = Lecturer(staffID=staffID, firstName=firstName, lastName=lastName, email=email, DOB=DOB)
        lecturer.save()
        return lecturer

    def update_lecturer(self, staffID, firstName, lastName, email, DOB):
        self.staffID = staffID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.DOB = DOB
        self.save()
        return self

    def delete_lecturer(self):
        self.delete()

    @staticmethod
    def get_lecturer(lecturer_id):
        try:
            lecturer = Lecturer.objects.get(pk=lecturer_id)
            return lecturer
        except Lecturer.DoesNotExist:
            return None


class Student(models.Model):
    studentID = models.CharField(max_length=50)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    email = models.EmailField()
    DOB = models.DateField()

    @classmethod
    def create_student(cls, studentID, firstName, lastName, email, DOB):
        student = cls(studentID=studentID, firstName=firstName, lastName=lastName, email=email, DOB=DOB)
        student.save()
        return student

    def update_student(self, studentID, firstName, lastName, email, DOB):
        self.studentID = studentID
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.DOB = DOB
        self.save()
        return self

    def delete_student(self):
        self.delete()

    @staticmethod
    def get_student(student_id):
        try:
            student = Student.objects.get(pk=student_id)
            return student
        except Student.DoesNotExist:
            return None


class Class(models.Model):
    number = models.CharField(max_length=50)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')

    def create_class(self, number, semester, course, lecturer):
        _class = Class(number=number, semester=semester, course=course, lecturer=lecturer)
        _class.save()
        return _class

    def update_class(self, number, semester, course, lecturer):
        self.number = number
        self.semester = semester
        self.course = course
        self.lecturer = lecturer
        self.save()
        return self

    def delete_class(self):
        self.delete()

    @staticmethod
    def get_class(class_id):
        try:
            _class = Class.objects.get(pk=class_id)
            return _class
        except Class.DoesNotExist:
            return None


class StudentEnrollment(models.Model):
    studentID = models.ForeignKey('Student', on_delete=models.CASCADE)
    classID = models.ForeignKey('Class', on_delete=models.CASCADE)
    grade = models.CharField(max_length=50)
    enrolTime = models.DateTimeField(auto_now_add=True)
    gradeTime = models.DateTimeField(null=True)

    @classmethod
    def create_enrollment(cls, studentID, classID, grade):
        enrollment = cls(studentID=studentID, classID=classID, grade=grade)
        enrollment.save()
        return enrollment

    def update_enrollment(self, studentID, classID, grade):
        self.studentID = studentID
        self.classID = classID
        self.grade = grade
        self.save()
        return self

    def delete_enrollment(self):
        self.delete()

    @staticmethod
    def get_enrollment(enrollment_id):
        try:
            enrollment = StudentEnrollment.objects.get(pk=enrollment_id)
            return enrollment
        except StudentEnrollment.DoesNotExist:
            return None
