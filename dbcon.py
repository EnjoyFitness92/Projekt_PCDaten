import pyodbc

def connect():
    try:
        con_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=G:\Projekt Inventardb\Inventar.accdb;'
        conn = pyodbc.connect(con_string)
        print("Connected To Database")
    except pyodbc.Error as e:
        print("Error in Connection", e)