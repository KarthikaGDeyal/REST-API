from django.urls import path
from APIApp import views

urlpatterns=[
path('Productpage/',views.Productpage,name="Productpage")
]