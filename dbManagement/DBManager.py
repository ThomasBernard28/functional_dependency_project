from sqlite3 import *
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

    
    def searchKeys(self, tableName):
        attributs = self.getTableAttributs(tableName)  # all attributes of the table (list of attributes)
        DF        = []                                 # all DF's of the table (list of tuples)
        DFleft    = []                                 # lhs
        DFright   = []                                 # rhs

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

        DF = self.getAllDF(tableName)
        
        keys = []
        for a in attributs:         # puts attributes that are not in the DFright list in the keys list
            if a not in DFright:
                keys.append(a)
        keyLen = len(keys)
        pointer = 0

        for rhs in DFright:
            if rhs in keys:
                keys.remove(rhs)
        
        current = keys[0]
        while pointer < keyLen:
            if current in DFleft:
                keys.append(DFright[DFleft.index(current)])
                current = DFright[DFleft.index(current)]
            else :
                found = False
                for l in DFleft:
                    if current in l.split():
                        keys.append(DFright[DFleft.index(l)])
                        current = DFright[DFleft.index(l)]               
                        found = True
               
                if not found:
                    pointer += 1
                    current = keys[pointer]

        return keys[:keyLen]
    
    def displayKeys(self, tableName):
        keys = self.searchKeys(tableName)
        return ''.join(keys)

    def getForm(self, tableName):
        if self.checkBCNF(tableName):
            print("The table is in BCNF (and indeed in 3NF)")
        else:
            print("not yet implemented")
         
    def checkBCNF(self, tableName):
        keys = list(self.searchKeys(tableName))
       
        DF        = []  # all DF's of the table (list of tuples)
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

        for att in keys:
            if (att in DFright) and (DFleft[DFright.index(att)] not in keys):
                problemDF.append(DF[DFright.index(att)])
        
        if problemDF == []:
            return True
        return False
