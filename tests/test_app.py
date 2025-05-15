# por nomenclatura, todos os testes começam por 'test_' seguido do modulo que irá ser testado

from http import HTTPStatus
from fastapi.testclient import TestClient
from fast_zero.app import app


def test_root_retorna_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
        - A: Arrange - Arranjo
        - A: ACT     - Executa a coisa (o SUT "System Under Test")
        - A: Assert  - Garanta que A é A
    """
    # Arrange
    client = TestClient(app)

    # ACT
    response = client.get('/')

    # Assert
    assert response.status_code == HTTPStatus.OK  # statuscode: 200
    assert response.json() == {'message': 'Hello world!'}
