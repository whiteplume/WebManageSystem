# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cheat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('days', models.IntegerField(max_length=32)),
                ('gameid', models.IntegerField(max_length=32)),
                ('name', models.CharField(max_length=20)),
                ('signature', models.CharField(max_length=4000)),
                ('discard', models.BooleanField()),
                ('type', models.SmallIntegerField()),
            ],
            options={
                'db_table': 'cheat',
            },
            bases=(models.Model,),
        ),
    ]
