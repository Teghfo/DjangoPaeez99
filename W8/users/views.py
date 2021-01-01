from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import RegisterSerializer
from .permissions import LocalOrIsAuthenticatedPermission


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny, ]


class PrivateView(APIView):
    permission_classes = [LocalOrIsAuthenticatedPermission, ]

    def get(self, request):
        return Response({'status': 'trusted!'})
