from django.shortcuts import render
from django.http import HttpResponse
from .models import Test

# Create your views here.

def projects(request):
    return render(request,'projects.html')

def index(request):
    test_data = Test()
    test_data.name = "Burger"
    test_data.desc = "Yummy and tasty"
    test_data.price = 150.00
    test_data.offer = False

    test_data2 = Test()
    test_data2.name = "Donut"
    test_data2.desc = "Sweeet"
    test_data2.price = 150.00
    test_data2.offer = True

    tests = [test_data,test_data2]

    return render(request,'index.html',{'tests':tests})

def lak(request):
    return HttpResponse("Hello World")

