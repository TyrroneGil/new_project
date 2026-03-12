from django.urls import path
from website_app import views
urlpatterns = [
    path('',views.renderIndex),
    path('addUser',views.fetchFromForm),
    path('deleteUser',views.deleteUser),
    path('updatePage',views.updatePage),
    path('updateInfo',views.updateInformation),
    path('test',views.test)
]