from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import response
from rest_framework import status

@api_view(["GET"])
def greet(request):
    

def greet(request):
    msg="Hello World"
    return render("greet.html",{"msg":msg})

# Create your views here.
