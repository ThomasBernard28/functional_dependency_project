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
            if records == []:
                return "The table is empty"
            return records

        except Error as error:
            print("Failed to read data from sqlite table", error)


    def addDF(self, tableName, lhs, rhs):
        try:
            self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
            records = self.cur.fetchall()
            FuncDepExist = False
            for tables in records:
                if tables != [] and 'FuncDep' in tables:
                    FuncDepExist = True

            if FuncDepExist:
                print("FuncDep is detected in your database")
                self.cur.execute("INSERT INTO FuncDep (tableName, lhs, rhs) VALUES (?, ?, ?)" , (tableName, lhs, rhs))
                self.conn.commit()
                print("Your DF was successfully added to the dfTable in your database")

            else:
                print("creating a new FuncDep table in your database")
                self.cur.execute(f"CREATE TABLE FuncDep (tableName TEXT NOT NULL, lhs TEXT NOT NULL, rhs TEXT NOT NULL)")

                self.cur.execute("INSERT INTO FuncDep (tableName, lhs, rhs) VALUES (?,?,?)", (tableName, lhs, rhs))

                self.conn.commit()
                print("Your DF was successfully added to the new dfTable in your database")

        except Error as error :
            print("Failed to add your DF, syntax might be incorect please be sure to enter  : \n dfTableName \n tableName \n lhs1 lhs2 lhsn \n rhs")
        

    def deleteDF(self, tableName, lhs, rhs):
        try:
            self.cur.execute("SELECT * FROM FuncDep WHERE tableName=\'{0}\' AND lhs=\'{1}\' AND rhs=\'{2}\'".format(tableName, lhs, rhs))
            records = self.cur.fetchall()
            if records == []:
                print("i'm here")
                raise exception("The DF you tried to remove does not exist, please try with other arguments")
            else:
                self.cur.execute("DELETE FROM FuncDep WHERE tableName=\'{0}\' AND lhs=\'{1}\' AND rhs=\'{2}\'".format(tableName, lhs, rhs))
                self.conn.commit()
                print("The DF was successfully deleted from the df table")

        except Error as error :
            print("The DB your entered does not exist.")


    def getAllDF(self, tableName):
        try:
            self.cur.execute("SELECT * FROM FuncDep WHERE tableName=\'{0}\'".format(tableName))
            records = self.cur.fetchall()
            if records == []:
                raise exception("No DF defined for this table. You can create them with our application")
            else:
                return records

        except Error as error:
            print("Failed to read data from sqlite table", error)

    def displayDF(self, tableName):
            records = self.getAllDF(tableName)
            result = "Here are all the DF(s) of the "+records[0][0]+ " table :\n"
            for DF in records : 
                result += DF[1] + " -----> " + DF[2] + "\n"
            print(result)


    def getTables(self):
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        records = self.cur.fetchall()
        for r in records[0]:
            print("> " + r + '\n')
