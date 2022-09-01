from django.contrib.auth import authenticate, login
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action, permission_classes, api_view

from .models import User
from .permissions import *
from .serializers import UserSerializer, LoginSerializer


# class LoginView(generics.RetrieveAPIView):
#     serializer_class= LoginSerializer
#     queryset=User.objects.all()

#     error_messages = {
#         'invalid': "Invalid username or password",
#         'disabled': "Sorry, this account is suspended",
#     }

#     def _error_response(self, message_key):
#         data = {
#             'success': False,
#             'message': self.error_messages[message_key],
#             'user_id': None,
#         }
#     def post(self,request):
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user = authenticate(email=email, password=password)
#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return Response(status=status.HTTP_100_OK)
#             return self._error_response('disabled')
        # return self._error_response('invalid')
    

# class UserViewSet(viewsets.ModelViewSet):
#     permission_classes = (IsCurrentSuperUser,)
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsCurrentSuperUser]
    

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsCurrentSuperUser]
        
class UserDetail(generics.RetrieveAPIView, generics.UpdateAPIView, generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsCurrentSuperUser]
    
    
# class RegisterView(generics.CreateAPIView):
    # pass
   
