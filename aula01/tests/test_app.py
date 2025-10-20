from http import HTTPStatus

from fastapi.testclient import TestClient

from src.aula01.app import app


def test_root_verifica_massage():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world'}


def test_html_verifica_conteudo():
    client = TestClient(app)

    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>This is a sample HTML response</h1>' in response.text
cd