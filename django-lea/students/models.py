from django.db import models

# Create your models here.

class Student(models.Model):
    roll_number = models.CharField(max_length=10)
    student_name = models.CharField(max_length=30)
    student_Email = models.CharField(max_length=30)
    student_phone = models.CharField(max_length=10)
    student_Address = models.CharField(max_length=30)
    

