from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Cliente
from .serializers import ClienteSerializer
class ClienteViewSet(viewsets.ModelViewSet):


    __basic_fields = ('nome', 'email')

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)

    filter_fields = __basic_fields
    search_fields = __basic_fields
