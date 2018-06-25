# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signatures', '0002_auto_20161123_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cheat',
            options={'managed': False},
        ),
    ]
