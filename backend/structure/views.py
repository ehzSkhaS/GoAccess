from rest_framework import viewsets

from .models import *
from .serializers import *
from authentication.permissions import *


class PlatformViewSet(viewsets.ModelViewSet):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    permission_classes = [IsCurrentSuperUser]
