from rest_framework import serializers

from .models import *

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Area
        fields = '__all__'


class RouteSuperAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteSuperArea
        fields = '__all__'


class RouteAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteArea
        fields = '__all__'


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'


class CheckpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Checkpoint
        fields = '__all__'


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = '__all__'


class RouteRoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = RouteRound
        fields = '__all__'

