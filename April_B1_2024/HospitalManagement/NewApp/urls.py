from django.conf.urls import url
from NewApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^pat/$',views.PatientAPI),
    url(r'^pat/([0-9]+)$',views.PatientAPI),
    url(r'^saveImage/$',views.saveImage)
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)