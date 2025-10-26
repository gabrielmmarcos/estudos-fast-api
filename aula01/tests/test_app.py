from http import HTTPStatus


def test_root_verifica_massage(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello world'}


def test_html_verifica_conteudo(client):
    response = client.get('/html')

    assert response.status_code == HTTPStatus.OK
    assert '<h1>This is a sample HTML response</h1>' in response.text


def test_create_user(client):
    user_data = {
        'username': 'testuser',
        'email': 'email@example.com',
        'password': 'securepassword',
    }
    response = client.post('/users/', json=user_data)
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'testuser',
        'email': 'email@example.com',
        'id': 1,
    }


def test_list_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'testuser',
                'email': 'email@example.com',
                'id': 1,
            }
        ]
    }
