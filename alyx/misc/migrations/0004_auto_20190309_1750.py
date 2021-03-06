# Generated by Django 2.1.4 on 2019-03-09 17:50
import uuid

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


def set_default_lab(apps, schema_editor):
    Lab = apps.get_model('misc', 'Lab')
    dlab = Lab.objects.filter(name=settings.DEFAULT_LAB_NAME)
    if dlab.count() == 0:
        Lab.objects.create(pk=settings.DEFAULT_LAB_PK, name=settings.DEFAULT_LAB_NAME)


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0003_auto_20190124_1025'),
        ('misc', '0003_auto_20190124_1025'),
    ]

    operations = [
        migrations.RunPython(set_default_lab),

        migrations.CreateModel(
            name='CageType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True,
                                                                        help_text='Structured data, formatted in a user-defined way',
                                                                        null=True)),
                ('description', models.CharField(blank=True, help_text='Extended description of the cage product/brand',
                                                 max_length=1023)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Enrichment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True,
                                                                        help_text='Structured data, formatted in a user-defined way',
                                                                        null=True)),
                ('name', models.CharField(help_text='Training wheel, treadmill etc..', max_length=255, unique=True)),
                ('description',
                 models.CharField(blank=True, help_text='Extended description of the enrichment, link ...',
                                  max_length=1023)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True,
                                                                        help_text='Structured data, formatted in a user-defined way',
                                                                        null=True)),
                ('name', models.CharField(help_text='Food brand and content', max_length=255, unique=True)),
                ('description',
                 models.CharField(blank=True, help_text='Extended description of the food, link ...', max_length=1023)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Housing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True,
                                                                        help_text='Structured data, formatted in a user-defined way',
                                                                        null=True)),
                ('cage_name', models.CharField(max_length=64)),
                ('cage_cleaning_frequency_days', models.IntegerField(blank=True, null=True)),
                ('light_cycle', models.IntegerField(blank=True, choices=[(0, 'Normal'), (1, 'Inverted')], null=True)),
                ('cage_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                to='misc.CageType')),
                ('enrichment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                                 to='misc.Enrichment')),
                ('food', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                           to='misc.Food')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HousingSubject',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, help_text='Long name', max_length=255)),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True,
                                                                        help_text='Structured data, formatted in a user-defined way',
                                                                        null=True)),
                ('start_datetime', models.DateTimeField()),
                ('end_datetime', models.DateTimeField(blank=True, null=True)),
                ('housing', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                              related_name='housing_subjects', to='misc.Housing')),
                ('subject', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL,
                                              related_name='housing_subjects', to='subjects.Subject')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='lab',
            name='cage_cleaning_frequency_days',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lab',
            name='light_cycle',
            field=models.IntegerField(blank=True, choices=[(0, 'Normal'), (1, 'Inverted')], null=True),
        ),
        migrations.AddField(
            model_name='housing',
            name='subjects',
            field=models.ManyToManyField(related_name='housings', through='misc.HousingSubject', to='subjects.Subject'),
        ),
        migrations.AddField(
            model_name='lab',
            name='cage_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='misc.CageType'),
        ),
        migrations.AddField(
            model_name='lab',
            name='enrichment',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='misc.Enrichment'),
        ),
        migrations.AddField(
            model_name='lab',
            name='food',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                    to='misc.Food'),
        ),
    ]
