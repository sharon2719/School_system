from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import PositiveSmallIntegerField
from django.db.models.fields import PositiveBigIntegerField
# from phonenumber_field.models
#create your models here
class Student(models.Model):
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    date_of_birth=models.DateField()
    email_address=models.EmailField()
    # phone_number=models.PhoneNumberField(unique=True,null=False,blank=False)
    nationality=models.CharField(max_length=30)
    national_id=models.CharField(max_length=16)
    student_id=models.PositiveSmallIntegerField()
    roll_number=models.CharField(max_length=6)
    Choices=(
        ('M',"Male"),
        ('F',"Female"),
        ('O','Other')
    )
    gender=models.CharField(max_length=10,choices=Choices)
    guardian_name=models.CharField(max_length=35)
    county_or_district=models.CharField(max_length=25)
    medical_report=models.FileField(upload_to='Uploads',blank='True')
    grade=models.CharField(max_length=3)
    date_of_enrollment=models.DateField()
    course_name=models.CharField(max_length=30)
    laptop_number=models.CharField(max_length=15)
    # languages=models.
    profile_photo=models.ImageField()
