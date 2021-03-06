# Generated by Django 2.2.10 on 2020-03-29 19:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0034_auto_20200328_1206'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteresourcelimits',
            name='client_body_limit',
            field=models.CharField(blank=True, default='', max_length=10, validators=[django.core.validators.RegexValidator(message='Must be either 1) blank for the default limit or 2) a number, optionally followed by one of the suffixes k/K or m/M.', regex='^(\\d+[kKmM]?)?$')]),
        ),
    ]
