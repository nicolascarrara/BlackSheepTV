# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 15:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blacksheep', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serie',
            name='nom',
        ),
        migrations.AddField(
            model_name='serie',
            name='firstAired',
            field=models.CharField(default='2000-0-0', max_length=10),
        ),
        migrations.AddField(
            model_name='serie',
            name='network',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='serie',
            name='overview',
            field=models.CharField(default='', max_length=600),
        ),
        migrations.AddField(
            model_name='serie',
            name='seriesName',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AddField(
            model_name='serie',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='serie',
            name='id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]
