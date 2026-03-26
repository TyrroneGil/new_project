from django.urls import path
from website_app import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSets

router = DefaultRouter()
router.register('users',UserViewSets)
urlpatterns = router.urls