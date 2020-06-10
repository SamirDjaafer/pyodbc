# Connecting Python with a DataBase

## First we need to connect to pyodbc using 

```python
import pyodbc
```

## Second we need to make a database class to represent our data base
## The values are:
```python
server = 'databases2.spartaglobal.academy'
database = 'Northwind'
username = 'SA'
password = 'Passw0rd2018'

connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
```

## We can make this into a class called DB. Everytime we want to use a new database we just need to replace the server, database, username and password values
```python
import pyodbc


class DB:
    def __init__(self, server='databases2.spartaglobal.academy', database='Northwind', username='SA', password='Passw0rd2018'):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.connection.cursor()


SpartaDB = DB()
```