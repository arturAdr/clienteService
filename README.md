
# API REST Clientes

## Tecnologias
Neste projeto foi usado as seguintes tecnologias,
Django framework,
Django REST Framework,
Linguagem de programação Python e
Banco de dados Sqlite3.

## Sobre o Projeto
[Django](https://www.djangoproject.com/) é um framework muito estável onde existe uma comunidade sempre trabalhando para melhorias
deixando sempre atualizado, corrigindo bugs e melhorando a segurança.

[Django REST](http://www.django-rest-framework.org/) foi usado para criar o API REST responsável pela integração, esse framework é bem robusto e atende as necessidades de um grande ou pequeno projeto umas da vantagens dele é a grande familiaridade com o Django tornando assim uma programação mais simples para manutenção e melhorias do projeto

Banco de dados [SQLite](https://www.sqlite.org/) foi usado neste projeto por ser default do Django e também  por ser um projeto pequeno ele atende todas as necessidades de forma aceitável.

### Manipuladores e Roteamento
**Método**|**URL**|**Ação**
:--:|:--:|:--:
POST|`http://127.0.0.1:8000/clientes/`|cria um novo cliente
GET|`http://127.0.0.1:8000/clientes/`|lista os clientes
GET|`http://127.0.0.1:8000/clientes/<id_cliente>/`|Detalhe do cliente
PUT|`http://127.0.0.1:8000/clientes/<id_cliente>/`|atualiza um cliente
DELETE|`http://127.0.0.1:8000/clientes/<id_cliente>/`|deleta um cliente
POST|`http://127.0.0.1:8000/listasDeDesejos/`|cria uma nova lista
GET|`http://127.0.0.1:8000/listasDeDesejos/`|lista as listas
GET|`http://127.0.0.1:8000/listasDeDesejos/<id_lista>/`|Detalhe da lista
PUT|`http://127.0.0.1:8000/listasDeDesejos/<id_lista>/`|atualiza uma lista
DELETE|`http://127.0.0.1:8000/listasDeDesejos/<id_lista>/`|deleta uma lista

**Estrutura Cliente**

```json
    {
        "nome": "Cliente de teste", // Nome do cliente
        "email": "teste@teste.com", // Email do Cliente,
        "lista_de_desejos": [
                "http://challenge-api.luizalabs.com/api/product/1bf0f365-fbdd-4e21-9786-da459d78dd1f"
        ] // Lista com links de produtos adicinados na lista de desejos
    }
```

**Estrutura ListaDeDesejo**

```json
    {
        "produto": "1bf0f365-fbdd-4e21-9786-da459d78dd1f", // Id do produto da api
        "cliente": 1 // id do cliente
    }
```

## Como rodar

Criei uma [docker](https://hub.docker.com/) e disponibilizei ela no [hub.docker.com](https://hub.docker.com/r/arturribeiro/clienteservice/)

Então para rodar o projeto é só executar o comando:

docker run -d -p 8000:8000 arturribeiro/clienteservice

O usuário da api é admin e a senha é admin123

Para a execução dos teste unitários é preciso entrar na docker com o seguinte comando:

docker exec -it id_da_docker bash 

E logo em seguida dentro da docker:

python manage.py test -v 2
