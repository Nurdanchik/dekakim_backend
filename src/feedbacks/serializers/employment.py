from rest_framework import serializers
from applications.models import EmploymentApplication


class EmploymentApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentApplication
        fields = [
            'id',
            'name',
            'surname',
            'phone_number',
            'email',
            'cv',
            'message',
        ]