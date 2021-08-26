from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import PositiveSmallIntegerField



class Student(models.Model):
    profile_photo=models.ImageField(upload_to="pictures/",null=True)
    first_name=models.CharField(max_length=12,null=True)
    last_name=models.CharField(max_length=12,null=True)
    age=models.PositiveSmallIntegerField(null=True)
    date_of_birth=models.DateField(null=True)
    email_address=models.EmailField(null=True)
    phone_number=models.CharField(max_length=13,null=True)
    nationality=models.CharField(max_length=30,null=True)
    national_id=models.CharField(max_length=16,null=True)
    student_id=models.PositiveSmallIntegerField(null=True)
    roll_number=models.CharField(max_length=6,null=True)
    Choices=(
        ('M',"Male"),
        ('F',"Female"),
        ('O','Other')
    )
    gender=models.CharField(max_length=10,choices=Choices,null=True)
    Choices=(
        ('A',"Arabic"),
        ('E',"English"),
        ('F',"French"),
        ('K',"Kiswahili"),
        ('Ki',"Kinyarwanda")
    )
    language=models.CharField(max_length=10,choices=Choices,null=True)
    guardian_name=models.CharField(max_length=35,null=True)
    county_or_district=models.CharField(max_length=25,null=True)
    medical_report=models.FileField(upload_to='documents/',null=True)
    grade=models.CharField(max_length=3,null=True)
    date_of_enrollment=models.DateField(null=True)
    course_name=models.CharField(max_length=30,null=True)
    laptop_number=models.CharField(max_length=15,null=True)
    