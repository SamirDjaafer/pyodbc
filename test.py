import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# print(connection)

cursor = connection.cursor()

# print(cursor)

query = cursor.execute('SELECT * FROM Products')

# print(query.fetchall())
rows = []

while True:
    row = cursor.fetchone()
    rows.append(row)
    if row == None:
        break
    print(row)

print(rows[0])




