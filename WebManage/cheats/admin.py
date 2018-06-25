# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from models import *
from django.http import HttpResponse 
import xlwt

class Ban_(admin.ModelAdmin):
    list_display = ('id', 'uid', 'record_id', 'unban_time')
    list_filter = ('unban_time', 'record_id')
    search_fields = ('unban_time', 'uid', 'record_id',)
    actions = ['export_data']

    def export_data(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=ban.xls'
        wb = xlwt.Workbook(encoding = 'utf-8')
        sheet = wb.add_sheet(u'ban')
        
        #1st line   
        sheet.write(0,0, 'uid')
        sheet.write(0,1, 'record_id')
        sheet.write(0,2, 'unban_time')

        default = xlwt.easyxf("align: horiz left")
        row = 1
        for data in queryset:
            sheet.write(row,0, data.uid, default)
            sheet.write(row,1, data.record_id, default)
            sheet.write(row,2, data.unban_time.strftime("%Y-%m-%d %H:%M:%S"), default)
            
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 100 * 50
            sheet.col(2).width = 150 * 50

            row += 1
           
        wb.save(response)
        return response
    export_data.short_description = "导出所选的 bans"

class BanRecord_(admin.ModelAdmin):
    list_display = ('id', 'uid', 'cheat_id', 'record_time')
    list_filter = ('record_time', 'cheat_id')
    search_fields = ('record_time', 'cheat_id', 'uid')
    actions = ['export_data']

    def export_data(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=banrecord.xls'
        wb = xlwt.Workbook(encoding = 'utf-8')
        sheet = wb.add_sheet(u'ban record')
        
        #1st line   
        sheet.write(0,0, 'uid')
        sheet.write(0,1, 'cheat_id')
        sheet.write(0,2, 'record_time')

        default = xlwt.easyxf("align: horiz left")
        row = 1
        for data in queryset:
            sheet.write(row,0, data.uid, default)
            sheet.write(row,1, data.cheat_id, default)
            sheet.write(row,2, data.record_time.strftime("%Y-%m-%d %H:%M:%S"), default)
            
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 100 * 50
            sheet.col(2).width = 150 * 50

            row += 1
           
        wb.save(response)
        return response
    export_data.short_description = "导出所选的 ban records"


admin.site.register(BanRecord, BanRecord_)
admin.site.register(Ban, Ban_)




