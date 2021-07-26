from .views import register_student
from django.urls import path

urlpatterns=[
    path('register',register_student,name='register_student')
]