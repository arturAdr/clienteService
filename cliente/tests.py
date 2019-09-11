from django.test import TestCase, Client
from django.contrib.auth.models import User
import base64
from model_mommy import mommy
from .models import Cliente

class TestCriacaoCliente(TestCase):

    def setUp(self):
        self.cliente = mommy.make(Cliente, nome='Cliente teste',
                               email='clienteTeste@teste.com.br')

    def test_criar_cliente(self):
        self.assertTrue(isinstance(self.cliente, Cliente))

class ClienteTestViewsPost(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': 'admin123'}

        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:admin123').decode()),
        }

    def test_criacao_cliente(self):

        data = {'nome': 'Cliente teste',
                'email': 'clienteTeste@teste.com.br'}

        response = self.client.post('/clientes/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 201)
        self.assertTrue(response.json()['nome'] == data['nome'])
    
    def teste_criacao_cliente_repetido(self):

        data = {'nome': 'Cliente teste',
                'email': 'clienteTeste@teste.com.br'}

        response = self.client.post('/clientes/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 201)

        response = self.client.post('/clientes/',  data, **self.auth_headers)

        self.assertTrue(response.status_code == 400)

class ClienteTestViewsGet(TestCase):

    def setUp(self):

        self.credentials = {
            'username': 'admin',
            'password': '123456789'}
        self.user = User.objects.create_user(**self.credentials)

        self.auth_headers = {
            'HTTP_AUTHORIZATION': 'Basic {}'.format(base64.b64encode(b'admin:123456789').decode()),
        }

        self.cliente_1 = mommy.make(Cliente, nome='cliente 01',
                                 email='cliente01@teste.com.br')

        self.cliente_2 = mommy.make(Cliente, nome='cliente 02',
                                 email='cliente02@teste.com.br')

    def test_listagem_cliente(self):

        response = self.client.get('/clientes/',  **self.auth_headers)
        self.assertTrue(response.status_code == 200)
        self.assertTrue(response.json()['count'] == 2)