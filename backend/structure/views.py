from rest_framework import generics

from .models import *
from .serializers import *
from ..authentication.permissions import *


class PlatformList(generics.ListAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    
    
class PlatformDetail(generics.RetrieveAPIView):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer
    # permission_classes = [IsCurrentUserOwner]