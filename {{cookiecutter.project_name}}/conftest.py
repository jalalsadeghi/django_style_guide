import pytest

from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from {{cookiecutter.project_slug}}.tests.factories import BaseUserFactory

@pytest.fixture
def api_client():
    user = User.objects.create_user('testuser', 'test@example.com', 'testpassword')
    client = APIClient()
    refresh = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

    return client


@pytest.fixture(scope='module')
def user1():
    print('Fixture for module')
    return BaseUserFactory