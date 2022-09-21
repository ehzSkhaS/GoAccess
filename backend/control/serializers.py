from rest_framework import serializers

from .models import *


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


class LicenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'


class SentryBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentryBox
        fields = '__all__'


class SentryBoxLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = SentryBoxLog
        fields = '__all__'


class CheckpointLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckpointLog
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'


class SupervisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervision
        fields = '__all__'


class DutyShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = DutyShift
        fields = '__all__'

