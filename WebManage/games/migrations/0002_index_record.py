# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gameid', models.IntegerField(max_length=32)),
                ('year', models.IntegerField(max_length=32)),
                ('month', models.IntegerField(max_length=32)),
                ('day', models.IntegerField(max_length=32)),
                ('hour', models.IntegerField(max_length=32)),
                ('record_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'index',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gameid', models.IntegerField(max_length=32)),
                ('name', models.CharField(unique=True, max_length=32)),
                ('signature', models.CharField(max_length=4000)),
                ('record_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'record',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
