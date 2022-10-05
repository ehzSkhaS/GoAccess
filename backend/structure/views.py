from utils.viewsets import ModelViewSetMixin

from .models import *
from .serializers import *


class PlatformViewSet(ModelViewSetMixin):
    queryset = Platform.objects.all()
    serializer_class = PlatformSerializer


class AgencyViewSet(ModelViewSetMixin):
    queryset = Agency.objects.all()
    serializer_class = AgencySerializer


class CondoViewSet(ModelViewSetMixin):
    queryset = Condo.objects.all()
    serializer_class = CondoSerializer
