from django.urls import path
from website_app import views
urlpatterns = [
    path('',views.renderIndex),
    path('testAdd',views.AddUserWithHash),
    path('auth',views.Authenticate),
    path('addTodo', views.addTodo),
    path('getTodo',views.readTodo),
    path('deleteTodo/<int:id>',views.deleteTodo)
]