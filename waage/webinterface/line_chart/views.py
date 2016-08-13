from django.shortcuts import render
from django.template import loader
from django.http import *
import json as simplejson
import sqlite3


def confirm_ajax(request):
    if (request.POST.has_key('date_to') and request.POST.has_key('date_from')):
        date_from=request.POST['date_from']
        date_from=date_from.encode('ascii', 'xmlcharrefreplace')
        print((date_from))
        data_from_day=date_from[3]
        data_from_day+=date_from[4]
        data_from_day=int(data_from_day)
        data_from_month=date_from[0]
        data_from_month+=date_from[1]
        data_from_month=int(data_from_month)
        data_from_year=date_from[6]
        data_from_year+=date_from[7]
        data_from_year=date_from[8]
        data_from_year+=date_from[9]
        data_from_year=int(data_from_year)
        date_to=request.POST['date_to']
        data_to_day=date_to[3]
        data_to_day+=date_to[4]
        data_to_day=int(data_to_day)
        data_to_month=date_to[0]
        data_to_month+=date_to[1]
        data_to_month=int(data_to_month)
        data_to_year=date_to[6]
        data_to_year+=date_to[7]
        data_to_year+=date_to[8]
        data_to_year+=date_to[9]
        data_to_year=int(data_to_year)
        print(data_to_year)

        response_dict={}
        response_dict.update({'test':'dd'})
        return HttpResponse(simplejson.dumps(response_dict))
    

def line_chart(request):
    connection = sqlite3.connect("../waage.db")
    cursor = connection.cursor()
    sql_command = """
    SELECT Datum from (SELECT * FROM waage order by ID desc limit 10) order by ID asc
    ;"""
    datum = cursor.execute(sql_command)
    datum = datum.fetchall()
    sql_command = """
    SELECT Gewicht from (SELECT * FROM waage order by ID desc limit 10) order by ID asc
    ;"""
    messwert = cursor.execute(sql_command)
    messwert = messwert.fetchall()
    connection.commit()
    connection.close()
    t=loader.get_template('line_chart/line_chart.html')
    c={"messwerte":messwert, "datum":datum}
    return HttpResponse(t.render(c, request))
        #return render(request, "line_chart/line_chart.html",{"messwerte":messwert, "datum":datum})


def test():
    connection = sqlite3.connect("../../waage.db")
    cursor = connection.cursor()
    sql_command = """
    SELECT Datum from (SELECT * FROM waage order by ID desc limit 10) order by ID asc
    ;"""
    datum = cursor.execute(sql_command)
    sql_command = """
    SELECT Gewicht from (SELECT * FROM waage order by ID desc limit 10) order by ID asc
    ;"""
    messwert = cursor.execute(sql_command)
    messwert = messwert.fetchall()
    print messwert[0][0]
    print type(messwert[0][0])
    connection.commit()
    connection.close()
    


if __name__ == "__main__":
    test()
# Create your views here.
