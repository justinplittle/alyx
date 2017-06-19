# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-29 10:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20170529_1136'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('electrophysiology', '0002_auto_20170426_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='extracellularrecording',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='extracellularrecording',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='spikesorting',
            name='mean_filtered_waveform',
        ),
        migrations.RemoveField(
            model_name='spikesorting',
            name='mean_unfiltered_waveform',
        ),
        migrations.AddField(
            model_name='extracellularrecording',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='The creator of the data.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_extracellularrecording_created_by_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='extracellularrecording',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='The creation date.', null=True),
        ),
        migrations.AddField(
            model_name='extracellularrecording',
            name='nominal_end_time',
            field=models.FloatField(blank=True, help_text='in seconds relative to session start', null=True),
        ),
        migrations.AddField(
            model_name='extracellularrecording',
            name='nominal_start_time',
            field=models.FloatField(blank=True, help_text='in seconds relative to session start.', null=True),
        ),
        migrations.AddField(
            model_name='intracellularrecording',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='The creator of the data.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_intracellularrecording_created_by_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='intracellularrecording',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='The creation date.', null=True),
        ),
        migrations.AddField(
            model_name='spikesortedunit',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='The creator of the data.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_spikesortedunit_created_by_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spikesortedunit',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='The creation date.', null=True),
        ),
        migrations.AddField(
            model_name='spikesorting',
            name='created_by',
            field=models.ForeignKey(blank=True, help_text='The creator of the data.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_spikesorting_created_by_related', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='spikesorting',
            name='created_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, help_text='The creation date.', null=True),
        ),
        migrations.AddField(
            model_name='spikesorting',
            name='extracellular_recording',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='electrophysiology.ExtracellularRecording'),
        ),
        migrations.AddField(
            model_name='spikesorting',
            name='mean_filtered_waveforms',
            field=models.ForeignKey(blank=True, help_text='mean filtered waveforms of every spike on every channel', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spike_sorting_filtered_waveforms', to='data.Dataset'),
        ),
        migrations.AddField(
            model_name='spikesorting',
            name='mean_unfiltered_waveforms',
            field=models.ForeignKey(blank=True, help_text='mean unfiltered waveforms of every spike on every channel', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spike_sorting_unfiltered_waveforms', to='data.Dataset'),
        ),
        migrations.AlterField(
            model_name='extracellularrecording',
            name='highpass_data',
            field=models.ForeignKey(blank=True, help_text='Extracellular high-passed data', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extracellular_recording_hpf', to='data.TimeSeries'),
        ),
        migrations.AlterField(
            model_name='extracellularrecording',
            name='lowpass_data',
            field=models.ForeignKey(blank=True, help_text='Extracellular low-passed data', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extracellular_recording_lpf', to='data.TimeSeries'),
        ),
        migrations.AlterField(
            model_name='extracellularrecording',
            name='raw_data',
            field=models.ForeignKey(blank=True, help_text='Raw electrophysiology recording data in flat binary format', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='extracellular_recording_raw', to='data.TimeSeries'),
        ),
        migrations.AlterField(
            model_name='extracellularrecording',
            name='session',
            field=models.ForeignKey(blank=True, help_text='The Session to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_extracellularrecording_session_related', to='actions.Session'),
        ),
        migrations.AlterField(
            model_name='intracellularrecording',
            name='session',
            field=models.ForeignKey(blank=True, help_text='The Session to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_intracellularrecording_session_related', to='actions.Session'),
        ),
        migrations.AlterField(
            model_name='spikesortedunit',
            name='session',
            field=models.ForeignKey(blank=True, help_text='The Session to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_spikesortedunit_session_related', to='actions.Session'),
        ),
        migrations.AlterField(
            model_name='spikesorting',
            name='session',
            field=models.ForeignKey(blank=True, help_text='The Session to which this data belongs', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='electrophysiology_spikesorting_session_related', to='actions.Session'),
        ),
        migrations.AlterField(
            model_name='spikesorting',
            name='spike_times',
            field=models.ForeignKey(blank=True, help_text='time of each spike relative to session start in universal seconds.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='spike_sorting_spike_times', to='data.Dataset'),
        ),
    ]