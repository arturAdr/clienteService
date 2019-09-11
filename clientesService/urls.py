from django.conf.urls import url, include
from rest_framework import routers

from cliente import views as views_cliente
from listaDeDesejos import views as views_lista_de_desejos

router = routers.DefaultRouter()
router.register(r'clientes', views_cliente.ClienteViewSet)
router.register(r'listasDeDesejos', views_lista_de_desejos.ListaDeDesejosViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]