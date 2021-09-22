from django.db import router
# from django.urls import 
from django.urls.conf import include,path
from rest_framework import routers, urlpatterns
from .views import EventViewSet, StudentViewSet,TrainerViewSet,CourseViewSet


router=routers.DefaultRouter()
router.register(r"students",StudentViewSet)
router.register(r"trainers",TrainerViewSet)
router.register(r"courses",CourseViewSet)
router.register(r"calendar",EventViewSet)

urlpatterns=[
    path("",include(router.urls),
    )
]