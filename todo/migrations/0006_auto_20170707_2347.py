# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-07 23:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_auto_20170703_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_django.UserSocialAuth'),
        ),
    ]
