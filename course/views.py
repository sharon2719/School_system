from django.db.models.aggregates import StdDev
from course.forms import CourseRegistrationForm
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Course

# Create your views here.
def register_course(request):
    form=CourseRegistrationForm

    if request.method == "POST":
        form=CourseRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=CourseRegistrationForm()
    return render (request,'register_course.html',{'form':form})


def course_list(request):
    courses=Course.objects.all()
    return render(request,"course_list.html",{'courses':courses})
    