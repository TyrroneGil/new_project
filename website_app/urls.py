from django.urls import path
from website_app import views
from rest_framework.routers import DefaultRouter
from .views import UserViewSets,ProfileViewSets

router = DefaultRouter()
router.register('users',UserViewSets)
router.register('profiles',ProfileViewSets)
urlpatterns = router.urls