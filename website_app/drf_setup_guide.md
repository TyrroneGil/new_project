# Django REST Framework Setup Guide

## 1. Install Django and DRF

``` bash
pip install django djangorestframework
```

## 2. Create Project and App

``` bash
django-admin startproject myproject
cd myproject
python manage.py startapp api
```

## 3. Add to INSTALLED_APPS

``` python
INSTALLED_APPS = [
    'rest_framework',
    'api',
]
```

## 4. Create a Model

``` python
# api/models.py
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
```

## 5. Run Migrations

``` bash
python manage.py makemigrations
python manage.py migrate
```

## 6. Create Serializer

``` python
# api/serializers.py
from rest_framework import serializers
from .models import Item

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'
```

## 7. Create ViewSet

``` python
# api/views.py
from rest_framework import viewsets
from .models import Item
from .serializers import ItemSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
```

## 8. Setup Router

``` python
# api/urls.py
from rest_framework.routers import DefaultRouter
from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet)

urlpatterns = router.urls
```

## 9. Connect URLs to Project

``` python
# myproject/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
```

## 10. Run Server

``` bash
python manage.py runserver
```

Visit: http://127.0.0.1:8000/api/items/

## Summary

-   Serializer converts model data to JSON
-   ViewSet handles CRUD operations
-   Router automatically creates routes

You're now ready to build APIs with Django REST Framework!
