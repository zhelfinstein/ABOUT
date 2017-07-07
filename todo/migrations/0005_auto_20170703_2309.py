# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-03 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_auto_20170703_2234'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]