from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.fields import Field

from .models import *
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


class SecuritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Security
        fields = '__all__'


class CondoAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = CondoAdmin
        fields = '__all__'


class AgencyAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgencyAdmin
        fields = '__all__'


class PlatformAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlatformAdmin
        fields = '__all__'


class ConfirmAccountSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    phone = serializers.CharField(required=True)
    address = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['first_name',
                  'last_name',
                  'phone',
                  'address',
                  'password'
                  ]

    def save(self, **kwargs):
        self.instance.first_name = self.validated_data['first_name']
        self.instance.last_name = self.validated_data['last_name']
        self.instance.phone = self.validated_data['phone']
        self.instance.address = self.validated_data['address']
        self.instance.password = make_password(self.validated_data['password'])
        self.instance.is_active = True
        self.instance.save()

