# -*- coding: utf-8 -*-
from django.shortcuts import render 

# Create your views here.
from django.http import HttpResponse 
import xlwt

import pymssql
#from cStringIO import StringIO
from models import *
from datetime import datetime


def exportgame(request):
    if Game.objects.all().count() < 60000:
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment;filename=game.xls'
        wb = xlwt.Workbook(encoding = 'utf-8')
        sheet = wb.add_sheet(u'game')
        
        #1st line   
        sheet.write(0,0, 'id')
        sheet.write(0,1, 'name')

        default = xlwt.easyxf("align: horiz left")
        row = 1
        for data in Game.objects.all():
            sheet.write(row,0, data.id, default)
            sheet.write(row,1, data.name, default)
            
            sheet.col(0).width = 100 * 50
            sheet.col(1).width = 100 * 50

            row += 1
           
        wb.save(response)
        return response

    else:
        return render(request, 'errors_export.html')

def exportrd(request):
    if Record.objects.all().count() < 60000:
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
        for data in Record.objects.all():
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


    else:
        return render(request, 'errors_export.html')


def line_index(request):
    lena = []
    for i in range(2010, 2017):       
        data = Index1.objects.filter(year=i).count()
        lena.append(data)

    lenb = []
    for i in range(2010, 2017):       
        data = Index2.objects.filter(year=i).count()
        lenb.append(data)

    lenc = []
    for i in range(2010, 2017):       
        data = Index3.objects.filter(year=i).count()
        lenc.append(data)
    return render(request, 'line_index.html', locals())

def column_index(request):
    lena = []
    for i in range(2010, 2017):       
        data = Index1.objects.filter(year=i).count()
        lena.append(data)

    lenb = []
    for i in range(2010, 2017):       
        data = Index2.objects.filter(year=i).count()
        lenb.append(data)

    lenc = []
    for i in range(2010, 2017):       
        data = Index3.objects.filter(year=i).count()
        lenc.append(data)
    return render(request, 'column_index.html', locals())

'''def pie_index(request):
    aa = Index1.objects.count()
    ab = Index2.objects.count()
    ac = Index3.objects.count()
    amount = aa+ab+ac
    aa_ = format(float(aa*100)/float(amount),'.2f')
    ab_ = format(float(ab*100)/float(amount),'.2f')
    ac_ = format(float(ac*100)/float(amount),'.2f')
    lena = []
    lenaa = []
    for i in range(2010, 2017):       
        data = Index1.objects.filter(year=i).count()
        data_ = format(float(data*100)/float(amount),'.2f')
        lena.append(data_)
        for j in range(12):       
            data = Index1.objects.filter(year=i).filter(month=j+1).count()
            data_ = format(float(data*100)/float(amount),'.2f')
            lenaa.append(data_)

    lenb = []
    lenbb = []
    for i in range(2010, 2017):
        data = Index2.objects.filter(year=i).count()
        data_ = format(float(data*100)/float(amount),'.2f')
        lenb.append(data_)
        for j in range(12):       
            data = Index2.objects.filter(year=i).filter(month=j+1).count()
            data_ = format(float(data*100)/float(amount),'.2f')
            lenbb.append(data_)

    lenc = []
    lencc = []
    for i in range(2010, 2017):       
        data = Index3.objects.filter(year=i).count()
        data_ = format(float(data*100)/float(amount),'.2f')
        lenc.append(data_)
        for j in range(12):       
            data = Index3.objects.filter(year=i).filter(month=j+1).count()
            data_ = format(float(data*100)/float(amount),'.2f')
            lencc.append(data_)

    return render(request, 'pie_index.html', locals())'''

def pie_index(request):
    aa = Index1.objects.count()
    ab = Index2.objects.count()
    ac = Index3.objects.count()
    amount = aa+ab+ac
    aa_ = format(float(aa*100)/float(amount),'.2f')
    ab_ = format(float(ab*100)/float(amount),'.2f')
    ac_ = format(float(ac*100)/float(amount),'.2f')
    return render(request, 'pie_index.html', locals())

def pie_game(request):
    aa = Index1.objects.count()
    ab = Index2.objects.count()
    ac = Index3.objects.count()
    amount = aa+ab+ac
    if request.GET.get("ID") and request.GET.get("YYYY"):
        d = request.GET.get("ID")
        yr = request.GET.get("YYYY")
        lena = []
        for i in range(12):
            data = Index.objects.filter(gameid=d).filter(year=yr).filter(month=i+1).count()
            data_ = format(float(data*100)/float(amount),'.2f')
            lena.append(data_)
        return render(request, 'pie_game_year.html', locals())
    elif request.GET.get("ID"):
        d = request.GET.get("ID")
        lena = []
        for i in range(2010, 2017):
            data = Index.objects.filter(gameid=d).filter(year=i).count()
            data_ = format(float(data*100)/float(amount),'.2f')
            lena.append(data_)
        return render(request, 'pie_game.html', locals())
    else:
        return render(request, 'errors_chart.html')

def line(request):
    if request.GET.get("YYYY") and request.GET.get("MM") and request.GET.get("DD"):
        yr = request.GET.get("YYYY")
        mth = request.GET.get("MM")
        dy = request.GET.get("DD")
        lena = []
        for i in range(24):       
            data = Index1.objects.filter(year=yr).filter(month=mth).filter(day=dy).filter(hour=i).count()
            lena.append(data)

        lenb = []
        for i in range(24):       
            data = Index2.objects.filter(year=yr).filter(month=mth).filter(day=dy).filter(hour=i).count()
            lenb.append(data)

        lenc = []
        for i in range(24):       
            data = Index3.objects.filter(year=yr).filter(month=mth).filter(day=dy).filter(hour=i).count()
            lenc.append(data)
        return render(request, 'line_day.html', locals())
    
    elif request.GET.get("YYYY") and request.GET.get("MM"):
        yr = request.GET.get("YYYY")
        mth = request.GET.get("MM")

##        if mth in [1,3,5,7,9,11]:
##            x = 31
##        elif mth in [4,6,8,10,12]:
##            x = 30
##        else:
##            x = 29
        lena = []
        for i in range(31):       
            data = Index1.objects.filter(year=yr).filter(month=mth).filter(day=i+1).count()
            lena.append(data)

        lenb = []
        for i in range(31):       
            data = Index2.objects.filter(year=yr).filter(month=mth).filter(day=i+1).count()
            lenb.append(data)

        lenc = []
        for i in range(31):       
            data = Index3.objects.filter(year=yr).filter(month=mth).filter(day=i+1).count()
            lenc.append(data)
        return render(request, 'line_month.html', locals())

    elif request.GET.get("YYYY"):
        yr = request.GET.get("YYYY")
        lena = []
        for i in range(12):       
            data = Index1.objects.filter(year=yr).filter(month=i+1).count()
            lena.append(data)

        lenb = []
        for i in range(12):       
            data = Index2.objects.filter(year=yr).filter(month=i+1).count()
            lenb.append(data)

        lenc = []
        for i in range(12):       
            data = Index3.objects.filter(year=yr).filter(month=i+1).count()
            lenc.append(data)
        return render(request, 'line_year.html', locals())

    else:
        return render(request, 'errors_chart.html')

    
def column(request):
    if request.GET.get("YYYY") and request.GET.get("MM") and request.GET.get("DD"):
        yr = request.GET.get("YYYY")
        mth = request.GET.get("MM")
        dy = request.GET.get("DD")
        lena = []
        for i in range(24):       
            data = Index1.objects.filter(year=yr).filter(month=mth).filter(day=dy).filter(hour=i).count()
            lena.append(data)

        lenb = []
        for i in range(24):       
            data = Index2.objects.filter(year=yr).filter(month=mth).filter(day=dy).filter(hour=i).count()
            lenb.append(data)

        lenc = []
        for i in range(24):       
            data = Index3.objects.filter(year=yr).filter(month=mth).filter(day=dy).filter(hour=i).count()
            lenc.append(data)
        return render(request, 'column_day.html', locals())
    
    elif request.GET.get("YYYY") and request.GET.get("MM"):
        yr = request.GET.get("YYYY")
        mth = request.GET.get("MM")
        lena = []
        for i in range(31):       
            data = Index1.objects.filter(year=yr).filter(month=mth).filter(day=i+1).count()
            lena.append(data)

        lenb = []
        for i in range(31):       
            data = Index2.objects.filter(year=yr).filter(month=mth).filter(day=i+1).count()
            lenb.append(data)

        lenc = []
        for i in range(31):       
            data = Index3.objects.filter(year=yr).filter(month=mth).filter(day=i+1).count()
            lenc.append(data)
        return render(request, 'column_month.html', locals())

    elif request.GET.get("YYYY"):
        yr = request.GET.get("YYYY")
        lena = []
        for i in range(12):       
            data = Index1.objects.filter(year=yr).filter(month=i+1).count()
            lena.append(data)

        lenb = []
        for i in range(12):       
            data = Index2.objects.filter(year=yr).filter(month=i+1).count()
            lenb.append(data)

        lenc = []
        for i in range(12):       
            data = Index3.objects.filter(year=yr).filter(month=i+1).count()
            lenc.append(data)
        return render(request, 'column_year.html', locals())

    else:
        return render(request, 'errors_chart.html')
        








    
