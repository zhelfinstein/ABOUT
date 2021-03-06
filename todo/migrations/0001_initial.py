# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-07-11 20:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.PositiveSmallIntegerField()),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Restriction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtype', models.CharField(choices=[('min', 'Minimum Duration (minutes)'), ('max', 'Maximum Duration (minutes)')], max_length=3)),
                ('cvalue', models.CharField(blank=True, max_length=20)),
                ('ivalue', models.IntegerField(blank=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.Item')),
            ],
        ),
    ]
