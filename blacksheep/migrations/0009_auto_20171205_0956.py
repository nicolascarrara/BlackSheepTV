# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-05 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacksheep', '0008_film_synopsis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serie',
            name='overview',
            field=models.CharField(default='', max_length=600, null=True),
        ),
    ]