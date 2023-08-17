import pytest
from django.urls import reverse
from rest_framework.test import APIClient

client = APIClient()

# @pytest.mark.django_db
# def test_registration_login():
#     client = APIClient()
#     # Start test registration
#     url_reg = reverse('rest_register')
#     data = {
#         'username': 'testuser',
#         'email': 'test@example.com',
#         'password1': 'testpassword',
#         'password2': 'testpassword',
#     }
#     reg_response = client.post(url_reg, data)
#
#     assert reg_response.status_code == 201
#     assert reg_response.data['user']['username'] == 'testuser'
#     assert reg_response.data['user']['email'] == 'test@example.com'
#
#     access = reg_response.data['access']
#     refresh = reg_response.data['refresh']
#
#     assert access != None
#     assert type(access) == str
#
#     assert refresh != None
#     assert type(refresh) == str
#
#     # End test registration
#
#     # Start test login
#     url_login = reverse('rest_login')
#     data = {
#         'username': 'testuser',
#         'email': 'test@example.com',
#         'password': 'testpassword',
#     }
#
#     login_response = client.post(url_login, data)
#     assert login_response.status_code == 200
#
#     access = reg_response.data['access']
#     refresh = reg_response.data['refresh']
#
#     assert access != None
#     assert type(access) == str
#
#     assert refresh != None
#     assert type(refresh) == str
#     # End test login
#
#     # Start test logout
#     url_logout = reverse('rest_logout')
#     data = {}
#     logout_response = client.post(url_logout, data)
#     assert logout_response.status_code == 200
#     # End test logout


# @pytest.mark.django_db
# def test_register_user(user1):
#     response = user1.create()
#     assert response.status_code == 201

@pytest.mark.django_db
def test_login_user(api_client):
    # # Start test logout
    # url_logout = reverse('rest_logout')
    # data = {}
    # logout_response = client.post(url_logout, data)
    # assert logout_response.status_code == 200
    # # End test logout

    url_login = reverse('rest_login')
    data = {
        'username': 'testuser',
        'email': 'test@example.com',
        'password': 'testpassword',
    }
    login_response = client.post(url_login, data)

    assert login_response.status_code == 200

# @pytest.mark.django_db
# def test_login_user(user1):
#     response = user1.create()
#
#     if response.status_code == 201:
#         # Start test logout
#         url_logout = reverse('rest_logout')
#         data = {}
#         logout_response = client.post(url_logout, data)
#         # End test logout
#         if logout_response.status_code == 200:
#             # Start test login
#             url_login = reverse('rest_login')
#             data = {
#                 'username': 'testuser',
#                 'email': 'test@example.com',
#                 'password': 'testpassword',
#             }
#             login_response = client.post(url_login, data)
            # assert login_response.status_code == 200
            #
            # access = login_response.data['access']
            # refresh = login_response.data['refresh']
            #
            # assert access != None
            # assert type(access) == str
            # print(access)
            # assert refresh != None
            # assert type(refresh) == str
            # # End test login



# @pytest.mark.django_db
# def test_logout_user(user1):
#     response = user1.create()
#
#     if response.status_code == 201:
#         # Start test logout
#         url_logout = reverse('rest_logout')
#         data = {}
#         logout_response = client.post(url_logout, data)
#         assert logout_response.status_code == 200
#         # End test logout
