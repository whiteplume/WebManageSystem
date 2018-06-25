# -*- coding: utf-8 -*-
from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse 
import xlwt
from models import *
#from cStringIO import StringIO


def exportsign(request):
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
    for data in Cheat.objects.all():
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
