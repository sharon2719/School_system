from .views import register_course,course_list
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('register/',register_course,name='register_course'),
    path('list/',course_list,name="course_list"),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)