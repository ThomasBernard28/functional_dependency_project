from sqlite3 import *
#Code from https://pynative.com/python-sqlite/


class DBManager:
    def __init__(self, dbName):
        self.conn, self.cur = self.connect(dbName)


    def connect(self, dbName):
        try:
            dbConnection = connect(dbName)
            cursor       = dbConnection.cursor()

            return dbConnection , cursor

        except Error as error:
            print("Error while connecting to sqlite", error)


    def disconnect(self):
        self.cur.close()
        self.conn.close()
        

    def showTable(self, table):
        try:
            self.cur.execute("""SELECT * FROM """ + table)
            records = self.cur.fetchall()

            return records

        except Error as error:
            print("Failed to read data from sqlite table", error) 
