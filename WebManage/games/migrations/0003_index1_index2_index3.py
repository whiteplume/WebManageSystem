# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_index_record'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index1',
            fields=[
                ('id', models.IntegerField(max_length=32, serialize=False, primary_key=True)),
                ('year', models.IntegerField(max_length=32)),
                ('month', models.IntegerField(max_length=32)),
                ('day', models.IntegerField(max_length=32)),
                ('hour', models.IntegerField(max_length=32)),
            ],
            options={
                'db_table': 'index1',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Index2',
            fields=[
                ('id', models.IntegerField(max_length=32, serialize=False, primary_key=True)),
                ('year', models.IntegerField(max_length=32)),
                ('month', models.IntegerField(max_length=32)),
                ('day', models.IntegerField(max_length=32)),
                ('hour', models.IntegerField(max_length=32)),
            ],
            options={
                'db_table': 'index2',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Index3',
            fields=[
                ('id', models.IntegerField(max_length=32, serialize=False, primary_key=True)),
                ('year', models.IntegerField(max_length=32)),
                ('month', models.IntegerField(max_length=32)),
                ('day', models.IntegerField(max_length=32)),
                ('hour', models.IntegerField(max_length=32)),
            ],
            options={
                'db_table': 'index3',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
