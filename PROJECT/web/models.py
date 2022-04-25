from django.contrib.auth import get_user_model
from django.db import models

from django.core.validators import  MinLengthValidator

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
        raise ValueError('Only numbers are allowed')


UserModel = get_user_model()


class Quotes(models.Model):
    QUOTES_TYPE_FIELD_MAX_LEN = 30
    QUOTES_DESCRIPTION_MAX_LEN = 300

    type = models.CharField(
        max_length=QUOTES_TYPE_FIELD_MAX_LEN,

    )

    description = models.CharField(
        max_length=QUOTES_DESCRIPTION_MAX_LEN,
        null=True,
        blank=True,

    )

    created = models.DateTimeField(
        auto_now_add=True,
        blank=True
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    class Meta:
        verbose_name_plural = "quotes"


class Projects(models.Model):
    PROJECT_NAME_MAX_LENGTH = 30
    PROJECT_DESCRIPTION_MAX_LENGTH = 100
    name = models.CharField(
        max_length=PROJECT_NAME_MAX_LENGTH,
        default="PROJECT NAME",
        blank=True,
        null=True,
    )

    description = models.CharField(
        max_length=PROJECT_DESCRIPTION_MAX_LENGTH,
        default="PROJECT DESCRIPTION",
    )

    class Meta:
        verbose_name_plural = "projects"


class Pricing(models.Model):
    pass


class Careers(models.Model):
    pass


class Portfolio(models.Model):
    PROJECT_NAME_MAX_LEN = 15
    DESCRIPTION_MAX_LENGTH = 300
    IMAGE_UPLOAD_TO_DIR = 'mediafiles'

    CONCEPT = 'CONCEPT'
    REALIZED = 'REALIZED'

    TYPES = [(i, i) for i in (CONCEPT, REALIZED)]

    description = models.CharField(
        max_length=DESCRIPTION_MAX_LENGTH
    )

    type = models.CharField(
        max_length=max(len(i) for (i, _) in TYPES),
        choices=TYPES,
    )

    image = models.ImageField(
        upload_to=IMAGE_UPLOAD_TO_DIR
    )

    name = models.CharField(
        max_length=PROJECT_NAME_MAX_LEN,
    )


class CV(models.Model):
    CV_MAX_LEN = 20
    filename = models.CharField(
        max_length=CV_MAX_LEN,
    )

    upload = models.FileField(
        upload_to='media/'
    )

    def __str__(self):
        return self.filename


class ContactModel(models.Model):
    FIRST_NAME_MIN_LEN = 2
    FIRST_NAME_MAX_LEN = 20

    LAST_NAME_MIN_LEN = 2
    LAST_NAME_MAX_LEN = 20

    PHONE_MAX_LEN = 15

    USERNAME_MAX_LENGTH = 25

    SUBJECT_NAME_MIN_LEN = 2
    SUBJECT_NAME_MAX_LEN = 20

    CONTENT_MAX_LENGTH = 500

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
        default='email@email.com'
    )

    phone_number = models.CharField(

        max_length=PHONE_MAX_LEN,
        validators=(
            only_numbers_validator,
        ),
        unique=True,

    )

    subject = models.CharField(
        default='Subject',
        max_length=SUBJECT_NAME_MAX_LEN,
        validators=(
            MinLengthValidator(SUBJECT_NAME_MIN_LEN),

        )
    )

    content = models.CharField(
        default='Content',
        max_length=CONTENT_MAX_LENGTH,
    )
