import pyodbc

server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# print(connection)

cursor = connection.cursor()

# Question 1
query1 = cursor.execute("SELECT COUNT(OrderID) AS 'OrderAmount' FROM Orders")
question1 = query1.fetchone()[0]
print(question1)

# Question 2
query2 = cursor.execute("select count(orders.OrderID) FROM Orders WHERE orders.ShipCity = 'Rio de Janeiro'")
question2 = query2.fetchone()[0]
print(question2)

# Question 3
query3 = cursor.execute("select count(orders.OrderID) FROM Orders WHERE orders.ShipCity IN ('Rio de Janeiro','Reims')")
question3 = query3.fetchone()[0]
print(question3)

def returnQuery(query):
    q = cursor.execute(query)
    answer = q.fetchone()[0]
    return answer

print(returnQuery("select count(orders.OrderID) FROM Orders WHERE orders.ShipCity IN ('Rio de Janeiro','Reims')"))


