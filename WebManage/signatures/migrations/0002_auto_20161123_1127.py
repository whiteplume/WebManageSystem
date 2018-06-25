# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signatures', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheat',
            name='days',
            field=models.IntegerField(help_text=b'\xe8\xa2\xab\xe7\xa6\x81\xe5\xa4\xa9\xe6\x95\xb0', max_length=32),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cheat',
            name='discard',
            field=models.BooleanField(help_text=b'\xe6\x98\xaf\xe5\x90\xa6\xe7\xa6\x81\xe7\x94\xa8'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cheat',
            name='gameid',
            field=models.ForeignKey(to='games.Game', db_column=b'gameid'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cheat',
            name='name',
            field=models.CharField(help_text=b'\xe5\xa4\x96\xe6\x8c\x82\xe5\x90\x8d\xe7\xa7\xb0', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='cheat',
            name='signature',
            field=models.CharField(help_text=b'\xe7\x89\xb9\xe5\xbe\x81\xe7\xa0\x81', max_length=4000),
            preserve_default=True,
        ),
    ]
