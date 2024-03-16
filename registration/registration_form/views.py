from django.shortcuts import render
from django.http import HttpResponse
from .models import userdetails  

def index(request):
    return render(request,'collect.html')

def userdetails_info(request):
    if request.method== "POST":
        Name=request.POST('name')
        Email=request.POST('email')
        Gender=request.POST('gender')
        lang=request.POST('lang')
        ph_no=request.POST('ph_no')
        age=request.POST('age')
        new = userdetails(name=Name,email=Email,gender=Gender,lang=lang,ph_no=ph_no,age=age)
        new.save()

    return render(request,'collect.html')