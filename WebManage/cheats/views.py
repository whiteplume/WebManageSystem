# -*- coding: utf-8 -*-
from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse 
import xlwt
from models import *

from datetime import datetime
#from cStringIO import StringIO

def exportbrd(request):
    if BanRecord.objects.all().count() < 60000:
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
        for data in BanRecord.objects.all():
            sheet.write(row,0, data.uid, default)
            sheet.write(row,1, data.cheat_id, default)
            sheet.write(row,2, data.record_time.strftime("%Y-%m-%d %H:%M:%S"), default)
                
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 100 * 50
            sheet.col(2).width = 150 * 50

            row += 1
            
        wb.save(response)
        return response
        
    else:
        return render(request, 'errors_export.html')
        

    

def exportban(request):
    if Ban.objects.all().count() < 60000:
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
        for data in Ban.objects.all():
            sheet.write(row,0, data.uid, default)
            sheet.write(row,1, data.record_id, default)
            sheet.write(row,2, data.unban_time.strftime("%Y-%m-%d %H:%M:%S"), default)
            
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 100 * 50
            sheet.col(2).width = 150 * 50

            row += 1
           
        wb.save(response)
        return response
    else:
        return render(request, 'errors_export.html')

