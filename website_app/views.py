from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import ApiDetails, TodoList, Users
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def renderIndex(request):
    details = list(ApiDetails.objects.all().values())
    return JsonResponse({"message":details})
@csrf_exempt
def fetchFromForm(request):
    if request.method == "POST":
        data = json.loads(request.body)

        username = data.get("username")
        password = data.get("password")
    return JsonResponse({"username":username,"password":password})

# def updateData(request):
#     if request.method == "POST":
#         uid = request.POST['id']
#         Users.objects.get(id=uid)


def AddUserWithHash(request):
    hashedPassword = make_password("testPass")
    user = Users.objects.create(
        username="Tyrrone",
        password=hashedPassword
    )
    return JsonResponse({"message":"Added Successfully"})


def Authenticate(request):
    user = Users.objects.get(id=8)
    if check_password('testPass123',user.password):
        return JsonResponse({"Message":"Correct Password"})
    else:
        return JsonResponse({"Messsage":"Incorrect Password"})

@csrf_exempt
def addTodo(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title = data.get("title")
        desc = data.get('description')
        status = data.get('status')
        TodoList.objects.create(title=title,description=desc)
        return JsonResponse({"message":"added successfully"})

def readTodo(request):
    if request.method == "GET":
        todolists=list(TodoList.objects.all().values())
        
        return JsonResponse({"lists":todolists})

def deleteTodo(request,id):
    if request.method == "GET":
        TodoList.objects.filter(id=id).delete()
        return JsonResponse({"message":'Deleted Successfully'})

    


