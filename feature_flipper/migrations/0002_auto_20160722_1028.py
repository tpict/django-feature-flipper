# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feature_flipper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='featureflipper',
            name='feature',
            field=models.CharField(choices=[(b'feature_for_all', 'Feature for everyone'), (b'restricted_feature', 'Restricted Feature')], max_length=200),
        ),
    ]
