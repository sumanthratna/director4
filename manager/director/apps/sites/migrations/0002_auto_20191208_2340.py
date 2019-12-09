# Generated by Django 2.2.8 on 2019-12-09 04:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='name',
            field=models.CharField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(2), django.core.validators.RegexValidator(message='Site names must consist of lowercase letters, numbers, underscores, and dashes. Dashes must go between two non-dash characters.', regex='^[a-z0-9_]+(-[a-z0-9_]+)*$')]),
        ),
    ]