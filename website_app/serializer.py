from rest_framework import serializers
from .models import TodoList

class TodoListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"