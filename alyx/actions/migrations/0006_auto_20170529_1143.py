# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 10:43
from __future__ import unicode_literals

import actions.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0005_auto_20170529_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surgery',
            name='location',
            field=models.ForeignKey(blank=True, default=actions.models._default_surgery_location, help_text='The physical location at which the surgery was performed', null=True, on_delete=django.db.models.deletion.CASCADE, to='equipment.LabLocation'),
        ),
    ]