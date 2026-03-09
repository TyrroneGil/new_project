from django.db import models

# Create your models here.
class Profile(models.Model):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)

class Post(models.Model):
    post_date = models.DateField(auto_created=True)
    poster = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post_description = models.TextField(max_length=244)

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)