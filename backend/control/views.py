from .models import RouteSuperArea, RouteArea, Route, Checkpoint, Round, License, SentryBox, DutyShift, Supervision, \
    Report
from .serializers import RouteSuperAreaSerializer, RouteAreaSerializer, RouteSerializer, CheckpointSerializer, \
    RoundSerializer, LicenceSerializer, SentryBoxSerializer, DutyShiftSerializer, SupervisionSerializer, \
    ReportSerializer
from backend.utils.viewsets import ModelViewSetMixin


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

# todo: Create CheckpointLog when user scan qr
