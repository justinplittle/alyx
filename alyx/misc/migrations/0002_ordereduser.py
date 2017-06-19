# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 10:31
from __future__ import unicode_literals

import django.contrib.auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('misc', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderedUser',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'ordering': ['username'],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]