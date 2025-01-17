"""
URL configuration for NewProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NewApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.Myclass.as_view()),
    path('new/',views.Newclass.as_view()),
    path('greetings/',views.Greetings_View.as_view()),
    path('add/',views.Addition.as_view()),
    path('sub/',views.Subtraction.as_view()),
    path('mul/',views.Multiplication.as_view()),
    path('div/',views.Division.as_view()),
    path('hi/',views.Factorial_View.as_view()),


]
