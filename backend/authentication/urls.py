from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()

# router.register('users', UserList)

# urlpatterns = [path('', include(router.urls)),]



# urlpatterns = [
#     path('login/', LoginView.as_view())    
# ]



urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
]

