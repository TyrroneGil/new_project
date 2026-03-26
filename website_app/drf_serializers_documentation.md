---
marp: true
theme: default
paginate: true
---


# Django REST Framework (DRF) Serializers Documentation

## Introduction

Django REST Framework (DRF) serializers are used to convert complex data
types such as Django models into JSON, and vice versa. They are
essential for API development because they allow data validation,
transformation, and representation.

---

## What is a Serializer?

A serializer: - Converts Django model instances into JSON
(serialization) - Converts JSON into Python objects 
(deserialization) - Validates incoming data

---

## Basic Serializer Example

``` python
from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()
    email = serializers.EmailField()
```

---

## ModelSerializer

A ModelSerializer automatically generates fields based on a Django
model.
---
### Example Model

``` python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
```
---
### Serializer

``` python
from rest_framework import serializers
from .models import Student

class StudentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```
---

## Serialization (Object → JSON)

``` python
student = Student.objects.get(id=1)
serializer = StudentModelSerializer(student)
print(serializer.data)
```

---

## Deserialization (JSON → Object)

``` python
data = {
    "name": "John",
    "age": 20,
    "email": "john@example.com"
}

serializer = StudentModelSerializer(data=data)

if serializer.is_valid():
    serializer.save()
```
---

## Validation

### Field-Level Validation

``` python
def validate_age(self, value):
    if value < 18:
        raise serializers.ValidationError("Age must be at least 18")
    return value
```

### Object-Level Validation

``` python
def validate(self, data):
    if data['name'] == "admin":
        raise serializers.ValidationError("Invalid name")
    return data
```

---

## Serializer Methods

-   `is_valid()` → Validates data
-   `save()` → Saves data to database
-   `data` → Serialized output
-   `errors` → Validation errors

---
## Nested Serializers

``` python
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True)

    class Meta:
        model = Student
        fields = '__all__'
```

---

## Serializer with Views (APIView)

``` python
from rest_framework.views import APIView
from rest_framework.response import Response

class StudentView(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentModelSerializer(students, many=True)
        return Response(serializer.data)
```

---

## Serializer with ViewSets

``` python
from rest_framework.viewsets import ModelViewSet

class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentModelSerializer
```

---

## Why Use Serializers?

-   Converts data easily to JSON
-   Built-in validation
-   Integrates with DRF views and viewsets
-   Reduces boilerplate code

---

## Conclusion

Serializers are a core component of Django REST Framework that simplify
API development by handling data conversion and validation. Using
ModelSerializer can significantly speed up development while maintaining
clean and readable code.

---

## Author Notes

This documentation is beginner-friendly and can be extended with
advanced topics like custom fields, hyperlinked serializers, and
pagination.
