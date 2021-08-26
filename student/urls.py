from .views import register_student,student_list
from django.urls import path




urlpatterns=[
    path('register/',register_student,name='register_student'),
    path('list/',student_list,name="student_list"),
]

