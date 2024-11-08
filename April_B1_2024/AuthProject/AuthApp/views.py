from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from AuthApp.models import User
from AuthApp.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
import datetime,jwt
# Create your views here.
class RegisterView(APIView):
    def post(self,request):
        obj=UserSerializer(data=request.data)
        obj.is_valid(raise_exception=True)
        obj.save()
        return Response(obj.data)

class LoginView(APIView):
    def post(self,request):
        email=request.data['email']
        password = request.data['password']
        x=User.objects.filter(email=email).first()
        if x is None:
            raise AuthenticationFailed("User not found...!!")
        if not x.check_password(password):
            raise AuthenticationFailed("Incorrect password..!")

        payload={
            'id':x.id,
            'exp':datetime.datetime.utcnow()+datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token=jwt.encode(payload,'secret',algorithm='HS256')


        response=Response()
        response.set_cookie(key='jwt',value=token,httponly=True)
        response.data={
            'jwt':token
        }
        return response

class UserView(APIView):
    def get(self,request):
        token=request.COOKIES.get('jwt')
        if not token:
            raise AuthenticationFailed("Unauthenticated...!")
        try:
            payload=jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Unauthenticated...!")
        user=User.objects.filter(id=payload['id']).first()
        x=UserSerializer(user)
        return Response(x.data)

class LogoutView(APIView):
    def post(self,request):
        x=Response()
        x.delete_cookie('jwt')
        x.data={
            "Message":"Logout success..!!"
        }
        return x