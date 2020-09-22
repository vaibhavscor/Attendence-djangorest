from rest_framework import serializers
from .models import Users_custom, Attendence


class User_customSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users_custom
        fields = '__all__'


class Attendence_user_serializer(serializers.ModelSerializer):
    class Meta:
        model = Attendence
        fields = ['user', 'Attendencein', 'Attendenceout']
