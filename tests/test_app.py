# por nomenclatura, todos os testes começam por 'test_' seguido do modulo que irá ser testado

from http import HTTPStatus


def test_root_retorna_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
        - A: Arrange - Arranjo
        - A: ACT     - Executa a coisa (o SUT "System Under Test")
        - A: Assert  - Garanta que A é A
    """
    # ACT
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK  # statuscode: 200
    assert response.json() == {'message': 'Hello world!'}


def test_create_user(client):
    """
    Teste: Criação de usuário via POST /users/

    Observações:
        - O campo 'id' não é enviado, pois é gerado automaticamente.
        - O schema de resposta é baseado em UserPublic (sem a senha).
    """

    response = client.post(
        '/users/',
        json={
            'username': 'Erlison',
            'password': 'secret',
            'email': 'erlison@example.com',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Erlison',
        'email': 'erlison@example.com',
    }


def test_read_users(client):
    """
    Testa a leitura da lista de usuários cadastrados.

    Este teste realiza uma requisição GET ao endpoint `/users/` e verifica se:
    - O status de resposta é HTTP 200 (OK).
    - O corpo da resposta contém a lista esperada de usuários com seus respectivos campos:
        - id
        - username
        - email
    """
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Erlison',
                'email': 'erlison@example.com',
            }
        ]
    }
