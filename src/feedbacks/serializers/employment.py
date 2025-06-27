from rest_framework import serializers
from feedbacks.models.employment import EmploymentApplication


class EmploymentApplicationCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmploymentApplication
        fields = ['name', 'surname', 'phone_number', 'email', 'cv', 'message']