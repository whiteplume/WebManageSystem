# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.IntegerField(max_length=32, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=32)),
            ],
            options={
                'db_table': 'game',
            },
            bases=(models.Model,),
        ),
    ]
