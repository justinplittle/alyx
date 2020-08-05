# Generated by Django 2.2.6 on 2020-07-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0003_auto_20200705_2046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(20, 'Waiting'), (25, 'Held'), (30, 'Started'), (40, 'Errored'), (45, 'Abandoned'), (50, 'Empty'), (60, 'Complete')], default=10),
        ),
    ]