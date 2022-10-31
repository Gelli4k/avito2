from datetime import date

import factory


class UserFactory(factory.django.DjangoModelFactory):
    first_name = 'test',
    last_name = 'testiy',
    username = 'johny_test',
    email = 'jh@test.ru',
    password = '12345',
    birthdate = factory.Faker('date_object')

    class Meta:
        model = 'users.User'


class SelectionFactory(factory.django.DjangoModelFactory):
    name = 'test_name'
    owner = factory.SubFactory(UserFactory)

    class Meta:
        model = 'ads.Selection'

class AdFactory(factory.django.DjangoModelFactory):
    name = 'Ad'
    author = factory.SubFactory(UserFactory)

    class Meta:
        model = 'ads.Ad'