from rest_framework.routers import SimpleRouter

from .views import *

router_auth = SimpleRouter()

router_auth.register('users', UserViewSet)
router_auth.register('security', SecurityViewSet)
router_auth.register('security/confirm-account', SecurityAccountConfirmViewSet)
router_auth.register('condominium-admin', CondoAdminViewSet)
router_auth.register('agency-admin', AgencyAdminViewSet)
router_auth.register('platform-admin', PlatformAdminViewSet)

