from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()


urlpatterns = [
    path('route-super-area/', RouteSuperAreaList),
    path('route-super-areas/<int:pk>/', RouteSuperAreaDetail.as_view()),
]