# -*- coding: utf-8 -*-
from django.db import models
#from games.models import *

# Create your models here.

game=((1,'cso'), (2,'cso2'),(3,'cso3'))
class Cheat(models.Model):
    days = models.IntegerField(max_length=32, help_text="被禁天数")
    game = models.CharField(max_length=1, choices=game, db_column="gameid")
    name = models.CharField(max_length=20, help_text="外挂名称")
    signature = models.CharField(max_length=4000, help_text="特征码")
    discard = models.BooleanField(help_text="是否禁用")
    type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'cheat'
