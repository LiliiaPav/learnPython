__author__ = 'lilii'
import pyodbc
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=desktop-27ni5gd\LiliiaPav;DATABASE=Study;UID=LiliiaOut;PWD=pythonconn')
cursor = cnxn.cursor()

cursor.execute("SELECT count(*) FROM [dbo].[test] where descrip='Cold Brew'")
for row in cursor.fetchall():
    print ('In table we have ' + str(row[0]) + ' Cold Brew')
cnxn.close()
