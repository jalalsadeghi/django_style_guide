import factory
import pytest


from rest_framework.test import APIClient
from django.urls import reverse


def register_f():
    client = APIClient()
    # Start test registration
    url_reg = reverse('rest_register')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password1': 'testpassword',
        'password2': 'testpassword',
    }
    reg_response = client.post(url_reg, data)

    return reg_response


@pytest.mark.django_db
class BaseUserFactory(factory.django.DjangoModelFactory):
    @classmethod
    def create(cls, **kwargs):
        reg_response = register_f()
        return reg_response
