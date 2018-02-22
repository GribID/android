import pyodbc


def zz(sqlreq):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=10.120.52.101;DATABASE=Patio;UID=it;PWD=it')
    cursor = cnxn.cursor()
    return cursor.execute(sqlreq)
