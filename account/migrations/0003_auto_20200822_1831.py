# Generated by Django 3.1 on 2020-08-22 17:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20200822_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(code='invalid_phone_number', message='Phone number must be valid eleven digits', regex='\\w{11}')]),
        ),
    ]