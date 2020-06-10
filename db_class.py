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

    def execute(self, what, where):
        self.cursor.execute(f'SELECT {what} FROM {where}')


SpartaDB = DB()

print(SpartaDB.connection)

print(SpartaDB.cursor)

