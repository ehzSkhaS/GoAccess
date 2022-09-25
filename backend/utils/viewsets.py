from rest_framework import viewsets
from authentication.permissions import IsCurrentSuperUser, IsOwnerOrReadOnly


class ModelViewSetMixin(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [IsCurrentSuperUser],
                                    'list': [IsCurrentSuperUser | IsOwnerOrReadOnly],
                                    'retrieve': [IsCurrentSuperUser | IsOwnerOrReadOnly],
                                    'update': [IsCurrentSuperUser],
                                    'partial_update': [IsCurrentSuperUser],
                                    'destroy': [IsCurrentSuperUser]}

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]