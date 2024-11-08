from django.conf.urls import url
from StudApp import views

urlpatterns=[
    url(r'^stud/$',views.StudentAPI),
    url(r'^stud/([0-9]+)$',views.StudentAPI),
    url(r'^teacher/$', views.TeacherAPI),
    url(r'^teacher/([0-9]+)$', views.TeacherAPI)
]
