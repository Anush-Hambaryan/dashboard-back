from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, LoginView
from knox import views as knox_views

from django.conf import settings 
from django.conf.urls.static import static

router = DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('logout/', knox_views.LogoutView.as_view()),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)