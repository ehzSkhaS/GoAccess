from utils.viewsets import ModelViewSetMixin

from .serializers import *
    

class RouteSuperAreaViewSet(ModelViewSetMixin):
    queryset = RouteSuperArea.objects.all()
    serializer_class = RouteSuperAreaSerializer


class RouteAreaViewSet(ModelViewSetMixin):
    queryset = RouteArea.objects.all()
    serializer_class = RouteAreaSerializer


class RouteViewSet(ModelViewSetMixin):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer


class CheckpointViewSet(ModelViewSetMixin):
    queryset = Checkpoint.objects.all()
    serializer_class = CheckpointSerializer


class RoundViewSet(ModelViewSetMixin):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class LicenceViewSet(ModelViewSetMixin):
    queryset = License.objects.all()
    serializer_class = LicenceSerializer


class SentryBoxViewSet(ModelViewSetMixin):
    queryset = SentryBox.objects.all()
    serializer_class = SentryBoxSerializer


class SupervisionViewSet(ModelViewSetMixin):
    queryset = Supervision.objects.all()
    serializer_class = SupervisionSerializer


class DutyShiftViewSet(ModelViewSetMixin):
    queryset = DutyShift.objects.all()
    serializer_class = DutyShiftSerializer


class ReportViewSet(ModelViewSetMixin):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class SentryBoxLogViewSet(ModelViewSetMixin):
    queryset = SentryBoxLog.objects.all()
    serializer_class = SentryBoxLogSerializer


class CheckpointLogViewSet(ModelViewSetMixin):
    queryset = CheckpointLog.objects.all()
    serializer_class = CheckpointLogSerializer
