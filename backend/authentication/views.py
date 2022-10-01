from utils.viewsets import ModelViewSetMixin

from .serializers import *


class UserViewSet(ModelViewSetMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    

class SecurityViewSet(ModelViewSetMixin):
    queryset = Security.objects.all()
    serializer_class = SecuritySerializer


class CondoAdminViewSet(ModelViewSetMixin):
    queryset = CondoAdmin.objects.all()
    serializer_class = CondoAdminSerializer


class AgencyAdminViewSet(ModelViewSetMixin):
    queryset = AgencyAdmin.objects.all()
    serializer_class = AgencyAdminSerializer


class PlatformAdminViewSet(ModelViewSetMixin):
    queryset = AgencyAdmin.objects.all()
    serializer_class = PlatformAdminSerializer
   
