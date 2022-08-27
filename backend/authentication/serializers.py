from rest_framework import serializers

from .models import User
from ..structure.models import *
from ..structure.serializers import *


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        
        
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            # 'password',
            'first_name',
            'last_name',
            'phone',
            'address',
            'image',
            'is_active',
            'is_staff',
            'is_superuser',
            # 'last_login',
            # 'created_date',
        ]
