from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()


urlpatterns = [
    # path('create-sentry-box-log/', CreateSentryBoxLog.as_view()),
    # path('create-checkpoint-log/', CreateCheckpointLog.as_view()),
]