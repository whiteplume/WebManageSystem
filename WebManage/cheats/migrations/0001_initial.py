# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.BigIntegerField(max_length=32)),
                ('record_id', models.IntegerField(max_length=32)),
                ('unban_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'ban',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BanRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uid', models.BigIntegerField(max_length=32)),
                ('cheat_id', models.IntegerField(max_length=32)),
                ('record_time', models.DateTimeField()),
            ],
            options={
                'db_table': 'banrecord',
            },
            bases=(models.Model,),
        ),
    ]
