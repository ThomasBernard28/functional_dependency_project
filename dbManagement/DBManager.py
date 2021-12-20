from sqlite3 import *
#Code from https://pynative.com/python-sqlite/

class DBManager:
    def __init__(self, dbName):
        self.conn, self.cursor = self.connect(dbName)

    def connect(self, dbName):
        try:
            dbConnection = connect(dbName)
            cursor = dbConnection.cursor()
            return dbConnection , cursor

        except Error as error:
            print("Error while connecting to sqlite")

    def disconnect(self):
        self.cursor.close()
        self.conn.close()
        
    def showTable(self, table):
        try:
            dbSelectQuery = """SELECT * FROM """ + table
            self.cursor.execute(dbSelectQuery)
            records = self.cursor.fetchall()
            print(records)

        except Error as error:
            print("Failed to read data from sqlite table", error)
