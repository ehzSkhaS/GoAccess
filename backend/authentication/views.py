from rest_framework.viewsets import ViewSetMixin
from rest_framework.generics import GenericAPIView
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
    queryset = PlatformAdmin.objects.all()
    serializer_class = PlatformAdminSerializer


class SecurityAccountConfirmViewSet(ModelViewSetMixin):
    queryset = User.objects.all()
    serializer_class = ConfirmAccountSerializer
    lookup_field = 'uuid'

    def get_queryset(self):
        if User.objects.filter(uuid=self.kwargs['uuid'], is_active=False):
            return self.queryset

        return None
