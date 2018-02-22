import pyodbc


def sr(sqlreq):
    return pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=10.120.52.101;'
                          'DATABASE=Patio;'
                          'UID=it;'
                          'PWD=it').cursor().execute(sqlreq)
