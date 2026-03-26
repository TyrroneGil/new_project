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

class ApiDetails(models.Model):
    id = models.IntegerField(blank=True, null=False,primary_key=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    ip_address = models.CharField(max_length=20, blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'api_details'


class TodoList(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    status = models.BooleanField(default=False)