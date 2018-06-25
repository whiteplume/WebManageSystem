# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

from cheats.models import *
from signatures.models import *


class Game(models.Model):
    id = models.IntegerField(primary_key=True, max_length=32)
    name = models.CharField(max_length=32, unique=True)

    class Meta:
        managed = False
        db_table = 'game'
    def __unicode__(self):
        return self.name

game=((1,'cso'), (2,'cso2'),(3,'cso3'))
class Record(models.Model):
    #gameid = models.IntegerField(primary_key=True, max_length=32,db_column="id")
    #gameid = models.IntegerField(max_length=32)
    game = models.CharField(max_length=1, choices=game, db_column="gameid")
    name = models.CharField(max_length=32, help_text="外挂名称")
    signature = models.CharField(max_length=4000, help_text="特征码")
    record_time = models.DateTimeField()
    days = models.IntegerField(max_length=32, help_text="被禁天数")
    class Meta:
        managed = False
        db_table = "record"

class Index(models.Model):
    gameid = models.IntegerField(primary_key=True, max_length=32)
    year = models.IntegerField(max_length=32)
    month = models.IntegerField(max_length=32)
    day = models.IntegerField(max_length=32)
    hour = models.IntegerField(max_length=32)
    class Meta:
        managed = False
        db_table = "index"

class Index1(models.Model):
    year = models.IntegerField(max_length=32)
    month = models.IntegerField(max_length=32)
    day = models.IntegerField(max_length=32)
    hour = models.IntegerField(max_length=32)
    class Meta:
        managed = False
        db_table = "index1"

class Index2(models.Model):
    year = models.IntegerField(max_length=32)
    month = models.IntegerField(max_length=32)
    day = models.IntegerField(max_length=32)
    hour = models.IntegerField(max_length=32)
    class Meta:
        managed = False
        db_table = "index2"

class Index3(models.Model):
    year = models.IntegerField(max_length=32)
    month = models.IntegerField(max_length=32)
    day = models.IntegerField(max_length=32)
    hour = models.IntegerField(max_length=32)
    class Meta:
        managed = False
        db_table = "index3"
