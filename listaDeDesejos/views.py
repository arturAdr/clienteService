from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters import rest_framework as filters
import requests 
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import ListaDeDesejos
from .serializers import ListaDeDesejosSerializer

class ListaDeDesejosViewSet(viewsets.ModelViewSet):

    __basic_fields = ('produto')

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    queryset = ListaDeDesejos.objects.all()
    serializer_class = ListaDeDesejosSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)

    def create(self, request):
        serializer = ListaDeDesejosSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            response = requests.get(url = 'http://challenge-api.luizalabs.com/api/product/{}'.format(request.data['produto']))
            if response.status_code == 200:
                return super().create(request)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)
