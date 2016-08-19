import sqlite3
import os.path

connection = sqlite3.connect("waage.db")
cursor = connection.cursor()

def create_db():
    sql_command = """
        CREATE TABLE waage (
        ID INTEGER PRIMARY KEY,
        Zeitstempel DATE,
        Datum DATE,
        Gewicht REAL,
        Versendet BOOL
        );"""
    cursor.execute(sql_command)
    connection.commit()

def write_db(data):
    sql_command = """
        INSERT INTO waage (ID, Zeitstempel, Datum, Gewicht, Versendet)
        VALUES(NULL, strftime('%s', 'now'), datetime('now'), """ + str(data) + """, NULL)
        ;"""
    cursor.execute(sql_command)
    connection.commit()

def close_db():
    connection.close()
    
if __name__=='__main__':
  #  create_db()
    write_db(222.22)
