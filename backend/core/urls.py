from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.urls import *
from control.urls import *
from structure.urls import *


router = DefaultRouter()

# authentication enndpoints
router.registry.extend(router_auth.registry)

# control enndpoints
router.registry.extend(router_control.registry)

# structure enndpoints
router.registry.extend(router_structure.registry)


urlpatterns = [
    path('manage/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
