from student.forms import StudentRegistrationForm
from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.
def register_student(request):
    form=StudentRegistrationForm
    return render (request,'register_student.html',{'form':form})