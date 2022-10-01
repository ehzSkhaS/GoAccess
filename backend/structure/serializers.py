from rest_framework import serializers

from .models import *


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = '__all__'


class AgencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Agency
        fields = '__all__'


class CondoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condo
        fields = '__all__'

