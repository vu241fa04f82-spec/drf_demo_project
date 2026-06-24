from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name', 'id', 'email', 'password', 'phone']

    def validate_phone(self, value):
        if value.startswith("91"):
            return value
        raise serializers.ValidationError(
            "Phone number must start with 91"
        )