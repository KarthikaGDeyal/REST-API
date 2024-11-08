from django.conf.urls import url
from EmpApp import views

urlpatterns=[
    url(r'^emp/$',views.EmployeeAPI),
    url(r'^emp/([0-9]+)$',views.EmployeeAPI)
]