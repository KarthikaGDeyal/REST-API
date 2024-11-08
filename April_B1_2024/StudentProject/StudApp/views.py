from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from StudApp.models import StudentDb,TeacherDb
from StudApp.serializers import Student_Serializer,Teacher_Serializer
from django.http.response import JsonResponse

@csrf_exempt
def StudentAPI(request,id=0):
  if request.method=="GET":
    x=StudentDb.objects.all()
    y=Student_Serializer(x,many=True)
    return JsonResponse(y.data,safe=False)
  elif request.method=="POST":
    p=JSONParser().parse(request)
    obj=Student_Serializer(data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data saved successfully..!",safe=False)
    return JsonResponse("Invalid data..!!",safe=False)
  elif request.method=="PUT":
    p = JSONParser().parse(request)
    x=StudentDb.objects.get(StudId=p['StudId'])
    obj=Student_Serializer(x,data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data Updated Successfully..!",safe=False)
    return JsonResponse("Failed to Update..!!", safe=False)
  elif request.method=="PATCH":
    p = JSONParser().parse(request)
    x=StudentDb.objects.get(StudId=p['StudId'])
    obj=Student_Serializer(x,data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data Updated Successfully..!",safe=False)
    return JsonResponse("Failed to Update..!!", safe=False)
  elif request.method=="DELETE":
    stud=StudentDb.objects.get(StudId=id)
    stud.delete()
    return JsonResponse("Data deleted..!!",safe=False)

@csrf_exempt
def TeacherAPI(request,id=0):
  if request.method=="GET":
    x=TeacherDb.objects.all()
    y=Teacher_Serializer(x,many=True)
    return JsonResponse(y.data,safe=False)
  elif request.method=="POST":
    p=JSONParser().parse(request)
    obj=Teacher_Serializer(data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data saved successfully..!",safe=False)
    return JsonResponse("Invalid data..!!",safe=False)
  elif request.method=="PUT":
    p = JSONParser().parse(request)
    x=TeacherDb.objects.get(TeacherId=p['TeacherId'])
    obj=Teacher_Serializer(x,data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data Updated Successfully..!",safe=False)
    return JsonResponse("Failed to Update..!!", safe=False)
  elif request.method=="PATCH":
    p = JSONParser().parse(request)
    x=TeacherDb.objects.get(TeacherId=p['TeacherId'])
    obj=Teacher_Serializer(x,data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data Updated Successfully..!",safe=False)
    return JsonResponse("Failed to Update..!!", safe=False)
  elif request.method=="DELETE":
    teacher=TeacherDb.objects.get(TeacherId=id)
    teacher.delete()
    return JsonResponse("Data deleted..!!",safe=False)