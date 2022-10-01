from rest_framework.routers import SimpleRouter

from .views import *

router_structure = SimpleRouter()

router_structure.register('condominium', CondoViewSet)
router_structure.register('agency', AgencyViewSet)
router_structure.register('platforms', PlatformViewSet)