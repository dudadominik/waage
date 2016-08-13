from django.shortcuts import render
from django.template import loader
from django.http import *
import json as simplejson
import sqlite3


def line_chart(request):
    if (request.POST.has_key('date_to') and request.POST.has_key('date_from')):
        date_from=request.POST['date_from']
        date_to=request.POST['date_to']
        print('******')
        print(date_to)
        print('******')
        response_dict={}
        response_dict.update({'test':'dd'})
        return HttpResponse(simplejson.dumps(response_dict))
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
