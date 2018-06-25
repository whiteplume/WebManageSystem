# -*- coding: utf-8 -*-
from django.db import models


class BanRecord(models.Model):
    uid = models.BigIntegerField(max_length=32)
    cheat_id = models.IntegerField(max_length=32)
    record_time = models.DateTimeField()
    
    class Meta:
        managed = False
        db_table = 'banrecord'

    
class Ban(models.Model):
    uid = models.BigIntegerField(max_length=32)
    record_id = models.IntegerField(max_length=32)
    unban_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'ban'

