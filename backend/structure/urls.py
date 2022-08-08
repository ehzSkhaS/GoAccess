from django.urls import path

from .views import *

urlpatterns = [
    path('platforms/', PlatformList.as_view()),
    path('platforms/<int:pk>/', PlatformDetail.as_view()),
]