from rest_framework import serializers
from django.contrib.auth.models import User
from django.core import validators

class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password']
        extra_kwargs = {'password': {'write_only': True, 'min_length':6}}