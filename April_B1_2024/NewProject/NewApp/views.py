import datetime
import math

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import datetime
# Create your views here.

class Myclass(APIView):
    def get(self,request):
        return Response({"Message":"Introduction to DRF"})

class Newclass(APIView):
    def get(self,request):
        return Response({"Hello":"GoodMorning"})

class Greetings_View(APIView):
    def get(self,*args):
        d=datetime.datetime.now()
        d_hour=d.hour
        msg=""
        if d_hour<12:
            msg = "Good Morning"
        elif d_hour<15:
            msg = "Good Afternoon"
        elif d_hour<18:
            msg = "Good Evening"
        else:
            msg = "Good Night"
        return Response({"Hello":msg})

class Addition(APIView):
    def post(self,request):
        print(request.data)
        x=request.data.get("num1")
        y = request.data.get("num2")
        sum=x+y
        return Response({"Result":sum})

class Subtraction(APIView):
    def post(self,request):
        print(request.data)
        x=request.data.get("num1")
        y = request.data.get("num2")
        difference=x-y
        return Response({"Result":difference})

class Multiplication(APIView):
    def post(self,request):
        print(request.data)
        x=request.data.get("num1")
        y = request.data.get("num2")
        product=x*y
        return Response({"Result":product})

class Division(APIView):
    def post(self,request):
        print(request.data)
        x=request.data.get("num1")
        y = request.data.get("num2")
        quotient=x/y
        return Response({"Result":quotient})

class Factorial_View(APIView):
    def post(self,request):
        x=request.data.get("num1")
        fact=math.factorial(x)
        return Response({"Factorial":fact})