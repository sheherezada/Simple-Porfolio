# Generated by Django 4.0.3 on 2022-04-12 09:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_projectuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='first_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('[A-Za-z ]', 'Only alpha characters are allowed.')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='last_name',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator('[A-Za-z ]', 'Only alpha characters are allowed.')]),
        ),
    ]