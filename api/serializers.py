from rest_framework import serializers
from student.models import Student
from trainer.models import Trainer
from course.models import Course
from school_calendar.models import Event

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=("first_name","last_name","age","title","age","date_of_birth","email_address","phone_number","nationality","national_id",
        "student_id","roll_number","gender","language","guardian_name","county_or_district","medical_report","grade","date_of_enrollment","course_name","laptop_number")
        
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trainer
        fields=("profile_photo","first_name","last_name","title","age","email_address","phone_number","nationality","county_or_district",
         "national_id","gender","bio","contract","date_hired","languages","course")


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model=Course
        fields=("course_name","course_code","course_trainer","course_schedule","syllabus","time_in_hours","course_duration")

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields=("title","description","start_time","end_time","venue")