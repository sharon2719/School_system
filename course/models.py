from django.db import models
from django.db.models import Model

# from durationfield.db.models.fields.duration import DurationField


# Create your models here.
class Course(models.Model):
    course_name=models.CharField(max_length=30)
    course_code=models.CharField(max_length=10)
    course_trainer=models.CharField(max_length=30)
    course_schedule=models.FileField(upload_to='documents/',blank='True')
    syllabus=models.TextField(max_length=300)
    time_in_hours=models.DurationField()
    course_duration=models.CharField(max_length=30)


