from django.shortcuts import render
from rest_framework.generics import GenericAPIView

class RegisterAgency(GenericAPIView):
    def post(self, request):
        pass

class RegisterAdmin(GenericAPIView):
    def post(self, request):
        pass