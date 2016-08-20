from django.shortcuts import render
from django.template import loader
from django.http import *
import json as simplejson
import sqlite3
import datetime
import time



def confirm_ajax(request):
    if (request.POST.has_key('date_to') and request.POST.has_key('date_from')):
        date_from=request.POST['date_from']
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

    now = datetime.datetime.now()
    year="%d" %now.year
    timestamp_of_current_year = datetime.date(int(year),1,1)
    timestamp_of_current_year= time.mktime(timestamp_of_current_year.timetuple())+3600
    timestamp_of_next_year = datetime.date(int(year)+1,1,1)
    timestamp_of_next_year= time.mktime(timestamp_of_next_year.timetuple())+3600
    sql_command ="""
    select count(Zeitstempel) from waage where  Zeitstempel > (?)  
    ;"""
    var=[timestamp_of_current_year]
    anzahl_messwerte_im_jahr = cursor.execute(sql_command,var)
    anzahl_messwerte_im_jahr = anzahl_messwerte_im_jahr.fetchall()
    anzahl_messwerte_im_jahr = anzahl_messwerte_im_jahr[0][0]
    id_steper = int(anzahl_messwerte_im_jahr)/10


    sql_command = """
    SELECT ID from waage order by ID desc
    ;"""
    last_id = cursor.execute(sql_command)
    last_id = last_id.fetchall()
    last_id = last_id[0][0]


    datum_array=[]    
    gewicht_array=[]
    for i in range(10):
        sql_command = """
        Select Datum from (select * from waage where Zeitstempel between (?) and (?) ) where ID = (?)
        ;"""
        var = [timestamp_of_current_year, timestamp_of_next_year, int(last_id-(id_steper*i))]
        datum = cursor.execute(sql_command, var)
        datum = datum.fetchall()
        datum_array.append(datum[0][0])
        sql_command = """
        Select Gewicht from (select * from waage where  Zeitstempel between (?) and (?)) where ID = (?)
        ;"""
        var = [timestamp_of_current_year, timestamp_of_next_year, int(last_id-(id_steper*i))]
        gewicht = cursor.execute(sql_command, var)
        gewicht = gewicht.fetchall()
        gewicht_array.append(gewicht[0][0])
        
    connection.commit()
    connection.close()
    t=loader.get_template('line_chart/line_chart.html')
    c={"messwerte":gewicht_array, "datum":datum_array}
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
