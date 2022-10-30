from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.exceptions import ValidationError

from datetime import date

USER_MIN_AGE = 9


def birthdate_validator(value):
    diff_years = relativedelta(date.today(), value).years()
    if diff_years < USER_MIN_AGE:
        raise ValidationError('Пользователь младше допустимого возраста')
    return value


class Location(models.Model):
    name = models.CharField(max_length=100)
    lat = models.DecimalField(max_length=8, decimal_places=6, max_digits=10, null=True)
    lng = models.DecimalField(max_length=8, decimal_places=6, max_digits=10, null=True)

    class Meta:
        verbose_name = 'Местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.name


class UserRoles(models.Model):
    USER = 'member'
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    choices = (
        (USER, 'Пользователь'),
        (ADMIN, 'Админ'),
        (MODERATOR, 'Модератор')
    )


# class User(models.Model):
#     first_name = models.CharField(verbose_name="Имя", help_text="Введите имя Пользователя до 60 знаков", max_length=60)
#     last_name = models.CharField(max_length=80)
#     username = models.CharField(max_length=20, unique=True)
#     password = models.CharField(max_length=60)
#     role = models.CharField(choices=UserRoles.choices, default='member', max_length=12)
#     locations = models.ManyToManyField(Location)
#     age = models.PositiveSmallIntegerField(null=True)
#     is_anonymous = models.BooleanField(default=0)
#     is_authenticated = models.BooleanField(default=0)
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     def __str__(self):
#         return f"Уважаемый {self.first_name} {self.last_name}"

class User(AbstractUser):
    role = models.CharField(choices=UserRoles.choices, default='member', max_length=12)
    locations = models.ManyToManyField(Location)
    age = models.PositiveSmallIntegerField(null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=200)
    birthdate = models.DateField(validators=[birthdate_validator])
    email = models.EmailField(unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"Уважаемый {self.first_name} {self.last_name}"
