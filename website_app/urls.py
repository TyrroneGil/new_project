from rest_framework.routers import DefaultRouter
from .views import TodoListViewSets

router = DefaultRouter()
router.register('todolists',TodoListViewSets)
urlpatterns = router.urls