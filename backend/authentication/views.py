from rest_framework import generics

from .models import User
from .permissions import *
from .serializers import UserSerializer

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    
class UserDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsCurrentUser]
    
    
class RegisterView(generics.CreateAPIView):
    pass
    
