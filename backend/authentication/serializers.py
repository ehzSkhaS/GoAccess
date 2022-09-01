from rest_framework import serializers

from .models import User
from structure.models import *
from structure.serializers import *

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        
        
class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()
    class Meta:
        model = User
        fields = [
            'id',
            'uuid',
            'email',
            # 'password',
            'first_name',
            'last_name',
            'phone',
            'address',
            'image',
            'is_active',
            'is_resident',
            'is_security',
            'is_supervisor',
            'is_residenceadmin',
            'is_condoadmin',
            'is_agencyadmin',
            'is_platformadmin',
            'is_staff',
            'is_superuser',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_date',
        ]
