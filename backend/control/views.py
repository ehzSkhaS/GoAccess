from django.db import transaction
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics, response
from .models import RouteSuperArea, RouteArea, Route, Checkpoint, Round, RouteRound
from .serializers import RouteSuperAreaSerializer, RouteAreaSerializer, RouteSerializer, CheckpointSerializer, RoundSerializer, RouteRoundSerializer


class RouteSuperAreaViewSet(viewsets.ModelViewSet):
    queryset = RouteSuperArea.objects.all()
    serializer_class = RouteSuperAreaSerializer


class RouteAreaViewSet(viewsets.ModelViewSet):
    queryset = RouteArea.objects.all()
    serializer_class = RouteAreaSerializer


class RouteViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class CheckpointViewSet(viewsets.ModelViewSet):
    queryset = Checkpoint.objects.all()
    serializer_class = CheckpointSerializer


class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class RouteRoundViewSet(viewsets.ModelViewSet):
    queryset = RouteRound.objects.all()
    serializer_class = RouteRoundSerializer
