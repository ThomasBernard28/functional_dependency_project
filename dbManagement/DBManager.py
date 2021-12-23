from sqlite3 import *
from tabulate import tabulate
import sys


class DBManager:
    def __init__(self, dbName):
        self.conn, self.cur = self.connect(dbName)


    def connect(self, dbName):
        """
        Method to open a connection to a local database
        """
        try:
            dbConnection = connect(dbName)
            cursor       = dbConnection.cursor()
            return dbConnection , cursor

        except:
            print("Error while connecting to sqlite")
            sys.exit(1)


    def disconnect(self):
        """
        Method to disconnect from the local database
        """
        self.cur.close()
        self.conn.close()
        

    def getTable(self, tableName):
        """
        This will return a list of tuple. Each tuple represent a row of the table in the database
        """
        try:
            self.cur.execute("""SELECT * FROM """ + tableName)
            records = self.cur.fetchall()
            if records == []:
                return "The table is empty"
            return records

        except:
            print("Failed to read data from sqlite table")
            sys.exit(1)


    def addDF(self, tableName, lhs, rhs):
        """
        This will add a new row in a FuncDep table of the database.
        If FuncDep doesn't exists, it is created
        """
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

        except:
            print("Failed to add your DF, syntax might be incorect please be sure to enter  : \n dfTableName \n tableName \n lhs1 lhs2 lhsn \n rhs")
            sys.exit(1)
        

    def deleteDF(self, tableName, lhs, rhs):
        """
        This will delete one DF in the FuncDep table of the database
        """
        try:
            self.cur.execute("SELECT * FROM FuncDep WHERE tableName=\'{0}\' AND lhs=\'{1}\' AND rhs=\'{2}\'".format(tableName, lhs, rhs))
            records = self.cur.fetchall()

            if records == []:
                print("The DF you tried to remove does not exist, please try with other arguments")

            else:
                self.cur.execute("DELETE FROM FuncDep WHERE tableName=\'{0}\' AND lhs=\'{1}\' AND rhs=\'{2}\'".format(tableName, lhs, rhs))
                self.conn.commit()
                print("The DF was successfully deleted from the df table")

        except:
            print("The DB your entered does not exist.")
            sys.exit(1)


    def deleteAllDF(self, tableName):
        """
        This will delete all DF about the given table in the FuncDep table of the database
        """
        try:
            self.cur.execute("SELECT * FROM FuncDep WHERE tablename=\'{0}\'".format(tableName))
            records = self.cur.fetchall()
            
            if records == []:
                print("There are no DF related to the table you entered to delete.")

            else:
                self.cur.execute("DELETE FROM FuncDep WHERE tableName=\'{0}\'".format(tableName))
                self.conn.commit()
                print("All the DF related to " + tableName + " were successfully deleted.")
        
        except:
            print("The DB you entered does not exist")
            sys.exit(1)


    def getAllDF(self, tableName):
        """
        This will return a list of tuple where each tuple is a DF about the given tabme.
        The DF are found in the FuncDep table of the database
        """
        try:
            self.cur.execute("SELECT * FROM FuncDep WHERE tableName=\'{0}\'".format(tableName))
            records = self.cur.fetchall()
            return records

        except:
            print("Failed to read data from sqlite table")
            sys.exit(1)


    def getAllTables(self):
        """
        This will return a list of all table's name of the database
        """
        self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = []
        for record in self.cur.fetchall():
            tables.append(record[0])
        return tables


    def getTableAttributs(self, tableName):
        attributs = []
        columns   = self.cur.execute(f"PRAGMA table_info({tableName})") # puts all attributes of the table in the attributes list
        for c in columns.fetchall():
            attributs.append(c[1])
        return attributs

    def getClosure(self, tableName, attrList):
        DF      = [] #all DF's of the table (list of tuples)
        DFright = []

        for df in self.getAllDF(tableName):  # get all lhs and rhs of the given table
            DF.append((df[0], df[1]))
            DFright.append(df[1])


        key = []

        for a in attrList:
            if a not in DFright:
                key.append(a)
        
        while True:
            old_key = key
            for df in DF:
                for d in DF:
                    if d[0] == df[1]:
                        key.append(d[1])
            if key == old_key:
                return key

    def displayKeys(self, tableName):
        keys = self.searchKeys(tableName)
        return ''.join(keys)

    def getForm(self, tableName):
        bcnf = self.checkBCNF(tableName)
        if bcnf[0]:
            print("The table is in BCNF (and indeed in 3NF)")
        else:
            print("The table is not in BCNF. Because of :")
            dfs = []
            for df in bcnf[1]:
                dfs.append(((df[0], df[1], "----->", df[2])))
            print(tabulate(dfs))
         

    def checkBCNF(self, tableName):
        keys = list(self.searchKeys(tableName))
       
        DF        = self.getAllDF(tableName)  # all DF's of the table (list of tuples)
        DFleft    = []  # lhs
        DFright   = []  # rhs

        for df in self.getAllDF(tableName):  # get all lhs and rhs of the given table
            DFleft.append(df[1])
            DFright.append(df[2])
        
        # le pire algorithme du 21è siècle : delete all duplicates in the lists and keep the elements order
        tmp = []
        for l in DFleft:
            if l not in tmp:
                tmp.append(l)
        DFleft = tmp[:]

        tmp = []
        for r in DFright:
            if r not in tmp:
                tmp.append(r)
        DFright = tmp[:]
        
        problemDF = []
        bcnf      = True

        for l in DFleft:
            r = DFright[DFleft.index(l)]
            if not r in l.split() and ''.join(l.split()) != ''.join(keys):
                problemDF.append((tableName, l, r))
                bcnf = False
        return (bcnf, problemDF)
