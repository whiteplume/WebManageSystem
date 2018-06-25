# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheats', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ban',
            options={'managed': False},
        ),
        migrations.AlterModelOptions(
            name='banrecord',
            options={'managed': False},
        ),
    ]
