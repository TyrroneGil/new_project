from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import ApiDetails, TodoList, Users
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def renderIndex(request):
    details = list(ApiDetails.objects.all().values())
    return render(request,'index.html')

def renderLogin(request):
    return render(request,'login.html')    

def renderHomePage(request):
    return render(request,'homepage.html')
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
    if request.method == "POST":
        username=request.POST['username']
        password = request.POST['password']
        hashedPassword = make_password(password)
        user = Users.objects.create(
            username=username,
            password=hashedPassword
        )
    return redirect('/login')


def Authenticate(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = Users.objects.get(username=username)
        if check_password(password,user.password):
            return redirect('/home')
        else:
            return redirect('/login')

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

    


