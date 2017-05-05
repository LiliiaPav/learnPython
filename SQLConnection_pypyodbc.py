import pypyodbc
connection = pypyodbc.connect('Driver={SQL Server}; Server=desktop-27ni5gd\LiliiaPav; Database=Study; uid=LiliiaOut;pwd=pythonconn')
cursor = connection.cursor()
SQLCommand = ("SELECT * FROM [dbo].[test]")
cursor.execute(SQLCommand)
results = cursor.fetchone()
while results:
     print (results)
     results = cursor.fetchone()
connection.close()
