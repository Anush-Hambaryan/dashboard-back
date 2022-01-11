from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from django.conf import settings 
from django.conf.urls.static import static 

router = DefaultRouter()
router.register(r'standardJobs', views.StandardJobViewSet, basename='standardJobs')
router.register(r'jobs5', views.Job5ViewSet, basename='jobs5')

urlpatterns = [
    path("", include(router.urls)),
]