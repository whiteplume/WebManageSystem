# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from models import *
from django.http import HttpResponse 
import xlwt


class Game_(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')
    list_filter = ('name',)
    actions = ['export_data']

    def export_data(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=game.xls'
        wb = xlwt.Workbook(encoding = 'utf-8')
        sheet = wb.add_sheet(u'game')
        
        #1st line   
        sheet.write(0,0, 'id')
        sheet.write(0,1, 'name')

        default = xlwt.easyxf("align: horiz left")
        row = 1
        for data in queryset:
            sheet.write(row,0, data.id, default)
            sheet.write(row,1, data.name, default)
            
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 100 * 50

            row += 1
           
        wb.save(response)
        return response
    export_data.short_description = "导出所选的 games"

admin.site.register(Game, Game_)


class Record_(admin.ModelAdmin):
    list_display = ('id', 'game', 'name', 'signature', 'record_time', 'days',)
    search_fields = ('name', 'signature', 'record_time')
    list_filter = ('game', 'name', 'record_time', 'days')
    ordering = ['id']
    actions = ['export_data']

    def export_data(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=record.xls'
        wb = xlwt.Workbook(encoding = 'utf-8')
        sheet = wb.add_sheet(u'record')
        
        #1st line   
        sheet.write(0,0, 'gameid')
        sheet.write(0,1, 'name')
        sheet.write(0,2, 'signature')
        sheet.write(0,3, 'record_time')
        sheet.write(0,4, 'days')

        default = xlwt.easyxf("align: horiz left")
        row = 1
        for data in queryset:
            sheet.write(row,0, data.game, default)
            sheet.write(row,1, data.name, default)
            sheet.write(row,2, data.signature, default)
            sheet.write(row,3, data.record_time.strftime("%Y-%m-%d %H:%M:%S"), default)
            sheet.write(row,4, data.days, default)
            
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 100 * 50
            sheet.col(2).width = 600 * 50
            sheet.col(3).width = 300 * 50
            sheet.col(4).width = 100 * 50

            row += 1

        wb.save(response)
        return response
    export_data.short_description = "导出所选的 records"
   
admin.site.register(Record, Record_)
