from rest_framework import viewsets

from .models import *
from .serializers import *
from authentication.permissions import *
from backend.utils.viewsets import ModelViewSetMixin


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsCurrentSuperUser]


class CondoViewSet(ModelViewSetMixin):
    queryset = Condo.objects.all()
    serializer_class = CondoSerializer
