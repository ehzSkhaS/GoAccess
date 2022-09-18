"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from authentication.views import UserViewSet, UserList, SecurityViewSet, CondoAdminViewSet, AgencyAdminViewSet, PlatformAdminViewSet
from structure.views import PlatformViewSet, CondoViewSet, AgencyViewSet
from control.views import RouteSuperAreaViewSet, RouteAreaViewSet, RouteViewSet, CheckpointViewSet, RoundViewSet, RouteRoundViewSet, LicenceViewSet, SentryBoxViewSet, DutyShiftViewSet, SupervisionViewSet, ReportViewSet

router = DefaultRouter()

router.register('users', UserViewSet)
router.register('platforms', PlatformViewSet)

router.register('security', SecurityViewSet)
router.register('condominium-admin', CondoAdminViewSet)
router.register('agency', AgencyViewSet)

router.register('agency-admin', AgencyAdminViewSet)
router.register('platform-admin', PlatformAdminViewSet)

router.register('condominium', CondoViewSet)

router.register('round', RoundViewSet)
router.register('route-round', RouteRoundViewSet)

router.register('route-super-area', RouteSuperAreaViewSet)
router.register('route-area', RouteAreaViewSet)
router.register('route', RouteViewSet)
router.register('checkpoint', CheckpointViewSet)
router.register('licence', LicenceViewSet)
router.register('sentry-box', SentryBoxViewSet)
router.register('duty-shift', DutyShiftViewSet)
router.register('supervision', SupervisionViewSet)
router.register('report', ReportViewSet)


urlpatterns = [
    path('manage/', admin.site.urls), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    # path('', include('authentication.urls')),
]

""" 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('rest_framework.urls')),
    path('', include('authentication.urls')),
    path('', include('structure.urls')),
]
 """
