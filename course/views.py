from django.db.models.aggregates import StdDev
from course.forms import CourseRegistrationForm
from django.shortcuts import render,redirect
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

    
def course_profile(request,id):
    course=Course.objects.get(id=id)
    return render(request,"course_profile.html",{"course":course})

def edit_course(request,id):
    course=Course.objects.get(id=id)
    if request.method=="POST":
        form=CourseRegistrationForm(request.POST,instance=course)
        if form.is_valid():
            form.save()
        return redirect("course_profile",id=course.id)
    else:
        form=CourseRegistrationForm(instance=course)
        return render(request,"edit_course.html",{"form":form})
