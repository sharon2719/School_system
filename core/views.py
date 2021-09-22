from school_calendar.views import event
from django.shortcuts import render
from student.models import Student
from trainer.models import Trainer
from course.models import Course
# from school_calendar.models import Event
# Create your views here.
def home(request):
    students=Student.objects.count()
    trainers=Trainer.objects.count()
    courses=Course.objects.count()
    # event=Event.objects.count()
    data={"students":students,"trainers":trainers,"courses":courses}
    return render(request,"home.html",data)

