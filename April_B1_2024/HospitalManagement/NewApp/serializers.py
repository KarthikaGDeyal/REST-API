from NewApp.models import PatientDb
from rest_framework import serializers

class Patient_Serializer(serializers.ModelSerializer):
    class Meta:
        model=PatientDb
        fields=(
            'PatientId',
            'Name',
            'Age',
            'Place',
            'Mobile',
            'Image'
        )