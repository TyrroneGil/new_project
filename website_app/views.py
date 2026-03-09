from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import Profile, Users
# Create your views here.
def renderIndex(request):
    users = Users.objects.all()
    return render(request,'index.html',{"users":users})

def fetchFromForm(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        Users.objects.create(username=username,password=password)
    return redirect('/')

# def updateData(request):
#     if request.method == "POST":
#         uid = request.POST['id']
#         Users.objects.get(id=uid)

def deleteUser(request):
    if request.method == "POST":
        uid = request.POST['id']
        Users.objects.filter(id=uid).delete()
    return redirect('/')

def updatePage(request):
    if request.method == "POST":
        uid = request.POST['id']
        user = Users.objects.get(id=uid)
        return render(request,'update.html',{"users":user})

def updateInformation(request):
    if request.method == "POST":
        uid = request.POST['id']
        newUsername = request.POST['newUsername']
        newPassword = request.POST['newPassword']
        Users.objects.filter(id = uid).update(username=newUsername,password=newPassword)
        return redirect('/')


