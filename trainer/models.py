from django.db import models
from django.db.models.enums import Choices
from django.db.models.fields import PositiveSmallIntegerField

# Create your models here.
class Trainer(models.Model):
    profile_photo=models.ImageField(upload_to='pictures/',null=True)
    first_name=models.CharField(max_length=12)
    last_name=models.CharField(max_length=12)
    age=models.PositiveSmallIntegerField()
    email_address=models.EmailField()
    phone_number=models.CharField(max_length=13)
    nationality=models.CharField(max_length=30)
    county_or_district=models.CharField(max_length=25)
    national_id=models.CharField(max_length=16)
    Choices=(
        ('M',"Male"),
        ('F',"Female"),
        ('O','Other')
    )
    gender=models.CharField(max_length=10,choices=Choices)
    bio=models.TextField(max_length=500)
    contract=models.FileField(upload_to='document/',blank='True')
    date_hired=models.DateField()
    languages=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
 
