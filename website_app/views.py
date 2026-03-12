from django.shortcuts import render,redirect
from django.http import JsonResponse
from .models import ApiDetails
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


def test(request):
    return JsonResponse({"message":"Hello"})


