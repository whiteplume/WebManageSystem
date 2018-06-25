# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.

from django.contrib.admin.widgets import FilteredSelectMultiple
from django.contrib.auth.models import User as djangouser, Group as djangogroup
from models import *
from django.http import HttpResponse 
import xlwt


class Cheat_(admin.ModelAdmin):
    list_display = ('id', 'name', 'signature', 'game', 'type', 'discard', 'days')
    list_filter = ('days', 'game')
    search_fields = ('name', 'days')
    actions = ['export_data']

    def export_data(self, request, queryset):
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=signature.xls'
        wb = xlwt.Workbook(encoding = 'utf-8')
        sheet = wb.add_sheet(u'特征码')
        
        #1st line   
        sheet.write(0,0, 'name')
        sheet.write(0,1, 'signature')
        sheet.write(0,2, 'gameid')
        sheet.write(0,3, 'type')
        sheet.write(0,4, 'discard')
        sheet.write(0,5, 'days')

        default = xlwt.easyxf("align: horiz left")
        row = 1
        for data in queryset:
            sheet.write(row,0, data.name, default)
            sheet.write(row,1, data.signature, default)
            sheet.write(row,2, data.game, default)
            sheet.write(row,3, data.type, default)
            sheet.write(row,4, data.discard, default)
            sheet.write(row,5, data.days, default)
            
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 300 * 50
            sheet.col(2).width = 50 * 50
            sheet.col(3).width = 50 * 50
            sheet.col(4).width = 200 * 50
            sheet.col(5).width = 50 * 50

            row += 1

        wb.save(response)
        return response 
    export_data.short_description = "导出所选的 cheats"
        


admin.site.register(Cheat, Cheat_)
