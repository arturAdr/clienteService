from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Cliente
from listaDeDesejos.models import ListaDeDesejos


class ListaDeDesejosSerializer(serializers.HyperlinkedRelatedField):

    view_name = 'listaDeDesejos'

    class Meta:
        model = ListaDeDesejos
        fields = ('produto', 'cliente')
    
    def get_url(self, obj, view_name, request, format):
        return 'http://challenge-api.luizalabs.com/api/product/{}'.format(obj.produto)

class ClienteSerializer(serializers.ModelSerializer):

    lista_de_desejos = ListaDeDesejosSerializer(read_only=True, many=True)

    class Meta:
        model = Cliente
        fields = ('nome', 'email', 'lista_de_desejos', 'id')