from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth import models as auth_models
from PROJECT.accounts.managers import ProjectUserManager
from django.core.validators import MinLengthValidator

"""
Validators
only_letters_validator -> only letters are allowed -> [A-Za-z ]
only_numbers_validator -> only numeric characters are allowed ->^[0-9]+$'
"""


def only_letters_validator(value):
    if not value.isalpha():
        raise ValueError('Only letters are allowed')

def only_numbers_validator(value):
    if not value.isnumeric():
        raise  ValueError('Only numbers are allowed')

class ProjectUser(auth_models.AbstractUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LENGTH = 25
    PHONE_MAX_LEN = 15
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH,
        unique=True,

    )
    phone = models.CharField(
        blank=True,
        null=True,
        max_length=PHONE_MAX_LEN,
        validators=(
            only_numbers_validator,
        ),
        unique=True,

    )

    email = models.EmailField(
        unique=True,
    )

    created = models.DateTimeField(
        blank=True,
        auto_now_add=True,
    )

    modified = models.DateTimeField(
        auto_now=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'username'

    objects = ProjectUserManager()


class Profile(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20

    EMAIL_MAX_LEN = 40
    PHONE_MAX_LEN = 15

    USERNAME_MAX_LENGTH = 25


    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LEN),
            only_letters_validator,

        ),

    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LEN),
            only_letters_validator,
        ),

    )

    email = models.EmailField(
        max_length=EMAIL_MAX_LEN,
        unique=True,

    )

    phone = models.CharField(

        max_length=PHONE_MAX_LEN,
        validators=(
            only_numbers_validator,
        ),
        unique=True,

    )

    user = models.OneToOneField(
        ProjectUser,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        ordering = ('last_name', 'first_name')
