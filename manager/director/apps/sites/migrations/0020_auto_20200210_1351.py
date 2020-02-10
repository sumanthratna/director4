# Generated by Django 2.2.10 on 2020-02-10 18:51

import director.apps.sites.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0019_auto_20200210_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockerimage',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET(director.apps.sites.models._docker_image_get_default_image), related_name='children', to='sites.DockerImage'),
        ),
    ]
