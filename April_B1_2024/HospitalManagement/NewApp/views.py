from django.core.files.storage import default_storage
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from NewApp.models import PatientDb
from NewApp.serializers import Patient_Serializer
from django.http.response import JsonResponse

@csrf_exempt
def PatientAPI(request,id=0):
  if request.method=="GET":
    x=PatientDb.objects.all()
    y=Patient_Serializer(x,many=True)
    return JsonResponse(y.data,safe=False)
  elif request.method=="POST":
    p=JSONParser().parse(request)
    obj=Patient_Serializer(data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data saved successfully..!",safe=False)
    return JsonResponse("Invalid data..!!",safe=False)
  elif request.method=="PUT":
    p = JSONParser().parse(request)
    x=PatientDb.objects.get(PatientId=p['PatientId'])
    obj=Patient_Serializer(x,data=p)
    if obj.is_valid():
      obj.save()
      return JsonResponse("Data Updated Successfully..!",safe=False)
    return JsonResponse("Failed to Update..!!", safe=False)
  elif request.method=="DELETE":
    pat=PatientDb.objects.get(PatientId=id)
    pat.delete()
    return JsonResponse("Data deleted..!!",safe=False)


@csrf_exempt
def saveImage(request):
  img=request.FILES['profile']
  obj=default_storage.save(img.name,img)
  return JsonResponse(obj,safe=False)