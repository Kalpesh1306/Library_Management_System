from arrow import now
from django.db import models
from django.utils.timezone import now
# Create your models here.
class Books(models.Model):
    sname = models.CharField(max_length=100,default="Default Name")
    branch =models.CharField(max_length=100,default="Default Branch")
    books_id = models.AutoField(primary_key=True)
    books_name = models.CharField(max_length=100)
    author = models.CharField(max_length=20)
    course_enrolled = models.CharField(max_length=20)
    enrollment_date = models.DateField(default=now)
    category = models.CharField(max_length=20)

    def __str__(self):
        return self.books_name


class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    email_id = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    date_of_birth = models.DateField(max_length=20)
    city = models.CharField(max_length=20)
    course_enrolled = models.CharField(max_length=20)
    enrollment_date = models.DateField(max_length=20)

    def __str__(self):
        return self.student_name

class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username

