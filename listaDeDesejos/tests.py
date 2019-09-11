from django.test import TestCase, Client
from django.contrib.auth.models import User
import base64
from model_mommy import mommy
from .models import ListaDeDesejos
from cliente.models import Cliente

class ListaDeDesejosTestViewsPost(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': 'admin123'}

        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:admin123').decode()),
        }
        self.cliente = mommy.make(Cliente, nome='cliente 01',
                                 email='cliente01@teste.com.br')

    def test_adicionar_item_lista_de_desejos(self):

        data = {'produto': '1bf0f365-fbdd-4e21-9786-da459d78dd1f',
                'cliente': self.cliente.pk}

        response = self.client.post('/listasDeDesejos/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 201)
    
    def test_adicionar_item_invalido_lista_de_desejos(self):

        data = {'produto': 'item_invalido',
                'cliente': self.cliente.pk}

        response = self.client.post('/listasDeDesejos/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 400)
    
    def test_adicionar_item_repetido_lista_de_desejos(self):

        data = {'produto': '1bf0f365-fbdd-4e21-9786-da459d78dd1f',
                'cliente': self.cliente.pk}

        response = self.client.post('/listasDeDesejos/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 201)
    
        response = self.client.post('/listasDeDesejos/',  data, **self.auth_headers)
        self.assertTrue(response.status_code == 400)
