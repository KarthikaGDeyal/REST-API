from EmpApp.models import EmpDb
from rest_framework import serializers

class Employee_Serializer(serializers.ModelSerializer):
    class Meta:
        model=EmpDb
        fields=(
            'EmpId',
            'Name',
            'Place',
            'Position'
        )