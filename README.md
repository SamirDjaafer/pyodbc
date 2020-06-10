# Connecting Python with a DataBase / Pyodbc
## Pyodbc is a Python package which acts as an API to connect and interact with a database.
## CRUD stands for Create, Read, Update, Delete. CRUD is how we interact with a database in Python. 
## In this project I am going to be creating a DB class which will represent pyodbc connection to the database. 
## I will be creating new data in the table, reading data in the table, updating the table, and deleting some data from the table.
## I will be doing this for the products and clients table and have them in seperate git branches to seperate them and also get more familiar with git branching.


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