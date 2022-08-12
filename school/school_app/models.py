from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique = True)
    subject = models.CharField(max_length=20)
    classes_taught = models.CharField(max_length=20)
    contact_number = models.IntegerField()



class Student(models.Model):
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=15)
    email = models.EmailField(unique = True)
    standard = models.IntegerField()
    section = models.CharField(max_length=5)
    stream = models.CharField(max_length=20)
    roll_number = models.IntegerField()
