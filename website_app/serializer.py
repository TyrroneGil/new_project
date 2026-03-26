from rest_framework import serializers
from .models import Users, Profile

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
    
class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"