from rest_framework import serializers

from .models import User
from structure.models import *
from structure.serializers import *

class UserSerializer(serializers.ModelSerializer):
    platforms = PlatformSerializer(read_only=True, many=True)
    agencies = AgencySerializer(read_only=True, many=True)
    condos = CondoSerializer(read_only=True, many=True)
    residences = ResidenceSerializer(read_only=True, many=True)
    
    class Meta:
        model = User
        # fields = '__all__'
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone',
            'address',
            'image',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
            'created_date',
            'platforms',
            'agencies',
            'condos',
            'residences',
        ]
        
