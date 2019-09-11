from rest_framework import serializers

from .models import Cliente, ListaDeDesejos


class ListaDeDesejosSerializer(serializers.ModelSerializer):

    class Meta:
        model = ListaDeDesejos
        fields = ('produto', 'cliente', 'id')
