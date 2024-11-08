from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from EmpApp.models import EmpDb
from EmpApp.serializers import Employee_Serializer
from django.http.response import JsonResponse

@csrf_exempt
def EmployeeAPI(request,id=0):
  if request.method=="GET":
    x = EmpDb.objects.all()
    y = Employee_Serializer(x, many=True)
    return JsonResponse(y.data,safe=False)
  elif request.method=="POST":
    p=JSONParser().parse(request)
    obj=Employee_Serializer(data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data saved successfully..!",safe=False)
    return JsonResponse("Invalid data..!!",safe=False)
  elif request.method=="PUT":
    p = JSONParser().parse(request)
    x=EmpDb.objects.get(EmpId=p['EmpId'])
    obj=Employee_Serializer(x,data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data Updated Successfully..!",safe=False)
    return JsonResponse("Failed to Update..!!", safe=False)
  elif request.method=="PATCH":
    p = JSONParser().parse(request)
    x=EmpDb.objects.get(EmpId=p['EmpId'])
    obj=Employee_Serializer(x,data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data Updated Successfully..!",safe=False)
    return JsonResponse("Failed to Update..!!", safe=False)
  elif request.method=="DELETE":
    emp=EmpDb.objects.get(EmpId=id)
    emp.delete()
    return JsonResponse("Data deleted..!!",safe=False)

