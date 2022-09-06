from rest_framework import viewsets

from .models import *
from .serializers import *
from backend.utils.viewsets import ModelViewSetMixin


class PlatformViewSet(ModelViewSetMixin):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class CondoViewSet(ModelViewSetMixin):
    queryset = Condo.objects.all()
    serializer_class = CondoSerializer


class AgencyViewSet(ModelViewSetMixin):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer
