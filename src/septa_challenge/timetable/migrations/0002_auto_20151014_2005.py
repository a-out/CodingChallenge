# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='station',
            old_name='station_name',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='station',
            name='line',
        ),
        migrations.AddField(
            model_name='station',
            name='fare_zone',
            field=models.CharField(default='CCP', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='station',
            name='lines',
            field=models.ManyToManyField(to='timetable.Line'),
        ),
    ]
