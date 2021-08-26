from django.db.models.aggregates import StdDev
from student.forms import StudentRegistrationForm
from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Student


# Create your views here.
def register_student(request,):
    if request.method=="POST":
        form=StudentRegistrationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form=StudentRegistrationForm()
    return render (request,'register_student.html',{'form':form,'name':'Sharon'})

def student_list(request):
    students=Student.objects.all()
    return render(request,"student_list.html",{"students":students})
    