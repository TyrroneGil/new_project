from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
def renderIndex(request):
    user = {
        "name":"Eloisa",
        "course":"BSIT"
    }
    return render(request,'index.html')

