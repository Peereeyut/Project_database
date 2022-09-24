from django.shortcuts import render
from django.http import HttpResponse
# from django.template import loader
# Create your views here.

def login(request):
    return render(request, "registration/login.html")
    # return HttpResponse("<h1>aaaaa</h1>")

def register(request):
    return render(request,"register.html")

def home(request):
    return render(request, "template.html")