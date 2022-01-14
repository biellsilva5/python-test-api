from urllib import response
import pytest
from app import create_app


def test_cpf_valid_but_not_blacklist():
    app = create_app()

    with app.test_client() as test_client:
        response = test_client.get('/052.837.290-44')
        assert response.status_code == 200
        assert b'FREE' in response.data

def test_cpf_valid_but_in_blacklist():
    app = create_app()

    with app.test_client() as test_client:
        response = test_client.get('/00000000000')
        assert response.status_code == 200
        assert b'BLOCK' in response.data

def test_cpf_invalid():
    app = create_app()

    with app.test_client() as test_client:
        response = test_client.get('/123.123.123')
        assert response.status_code == 400
        assert b'This CPF is not valid.' in response.data
