# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-22 10:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_features', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testfeatureflipper',
            name='feature',
            field=models.CharField(choices=[(b'feature_for_all', 'Feature for everyone'), (b'restricted_feature', 'Restricted Feature')], max_length=200),
        ),
    ]
