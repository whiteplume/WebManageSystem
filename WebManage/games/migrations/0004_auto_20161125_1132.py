# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0003_index1_index2_index3'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'managed': False},
        ),
    ]
