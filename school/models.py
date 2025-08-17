from django.db import models
from django.contrib.auth.models import AbstractUser

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
# class User(AbstractUser):
#     SHIFT_CHOICES=(
#         ('MORNING_SHIFT','Morning shift'),
#         ('DAY_SHIFT','Day shift'),
#         ('NIGHT_SHIFT','Night shift'),
#     )
#     LANG_CHOICES=(
#         ('UZBEK','Uzbek'),
#         ('ENGLISH','English'),
#         ('RUSSIAN','Russian'),
#     )
#     BLOOD_TYPE_CHOICES=(
#         ('A+','A+'),
#         ('A-','A-'),
#         ('B+','B+'),
#         ('B-','B-'),
#         ('AB+','AB+'),
#         ('AB-','AB-'),
#         ('O+','O+'),
#         ('O-','O-'),
#     )
#     GENDER_CHOICES=(
#         ('MALE','Male'),
#         ('FEMALE','Female'),
#     )
#     qr_code=models.ImageField(upload_to='users/qr_codes',blank=True,null=True)
#     teacher_rating=models.CharField(max_length=500,blank=True,null=True)
#     shift=models.CharField(max_length=20,choices=SHIFT_CHOICES,default=SHIFT_CHOICES[0][0])
#     study_lang=models.CharField(max_length=20,choices=LANG_CHOICES,default=LANG_CHOICES[0][0])
#     phone_number=models.CharField(max_length=20,null=True,blank=True)
#     address=models.CharField(max_length=500,blank=True,null=True)
#     blood_group=models.CharField(max_length=500,choices=BLOOD_TYPE_CHOICES,blank=True,null=True)    