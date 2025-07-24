from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    ROLE_CHOICES=(
        ('admin','Admin'),
        ('teacher','O‘qituvchi'),
        ('student','O‘quvchi'),
    )
    role=models.CharField(max_length=10,choices=ROLE_CHOICES)
    talaba_id=models.CharField(max_length=20,unique=True)
    
    def __str__(self):
        return self.username


class Teacher(models.Model):
    fio=models.CharField(max_length=100)
    subject=models.CharField(max_length=50)
    
    def __str__(self):
        return self.fio
    
class Subject(models.Model):
    name=models.CharField(max_length=50)
    teachers=models.ManyToManyField(Teacher,related_name='fanlar')
    def __str__(self):
        return self.name


    