from rest_framework.routers import SimpleRouter

from .views import *

router_control = SimpleRouter()

router_control.register('route-super-area', RouteSuperAreaViewSet)
router_control.register('route-area', RouteAreaViewSet)
router_control.register('route', RouteViewSet)
router_control.register('checkpoint', CheckpointViewSet)
router_control.register('round', RoundViewSet)
router_control.register('licence', LicenceViewSet)
router_control.register('sentry-box', SentryBoxViewSet)
router_control.register('supervision', SupervisionViewSet)
router_control.register('duty-shift', DutyShiftViewSet)
router_control.register('report', ReportViewSet)
router_control.register('sentry-box-log', SentryBoxLogViewSet)
router_control.register('checkpoint-log', CheckpointLogViewSet)