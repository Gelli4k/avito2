import pytest



from factories import SelectionFactory, UserFactory, AdFactory
from users.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from pytest_factoryboy import register

register(SelectionFactory)
register(UserFactory)
register(AdFactory)



@pytest.fixture
def api_client(db, user):
    # user = User.objects.create_user(
    #     first_name='john',
    #     last_name='test',
    #     username='johny',
    #     email='jh@test.ru',
    #     password='12345',
    # )
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTPAUTHORIZATION=f'Bearer {token.access_token}')
    return client
