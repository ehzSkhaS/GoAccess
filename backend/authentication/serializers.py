from rest_framework import serializers

from .models import *
        
        
class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.ReadOnlyField()
    created_date = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = [
            'id',
            'uuid',
            'email',
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
