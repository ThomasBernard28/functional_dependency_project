from sqlite3 import *

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


    def addDF(self, tableName, lhs, rhs):
        try:
            getTablesQuery = """SELECT name FROM sqlite_master WHERE type='table';"""
            self.cur.execute(getTablesQuery)
            records = self.cur.fetchall()

            if "dfTable" in records:
                self.cur.execute("INSERT INTO dfTable (tableName, lhs, rhs) VALUES (?,?,?)", (tableName, lhs, rhs))
                self.conn.commit()

            else:
                self.cur.execute("CREATE TABLE dfTable (tableName TEXT, lhs TEXT, rhs TEXT)")
                self.cur.execute("INSERT INTO dfTable (tableName, lhs, rhs) VALUES (?,?,?)", (tableName, lhs, rhs))
                self.conn.commit()
                print("Your DF was successfully added to the dfTable in your database")

        except Error as error :
            print("Failed to add your DF, syntax might be incorect please be sure to enter  : tableName \n lhs1 lhs2 lhsn \n rhs")
        

    def deleteDF(self, tableName, lhs, rhs):
        try:
            self.cur.execute("DELETE FROM dftable WHERE tableName=\'"+tableName+"\' AND lhs=\'"+lhs+"\' AND rhs=\'" +rhs+"\'")
            self.conn.commit()
            print("The DF was successfully deleted from the df table")

        except Error as error :
            print("The DF you tried to remove does not exist, please try with other arguments")
