from sqlite3 import *

#Code from https://pynative.com/python-sqlite/
def connection(dbName):
    try:
        
        dbConnection = connect(dbName)
        cursor = dbConnection.cursor()
        print("Database created and successfully connected to SQLite")

        dbQuerySelection = "select sqlite_version()"
        cursor.execute(dbQuerySelection)
        record = cursor.fetchall()
        print("SQLite Database Version is: " , record)
        cursor.close()

    except Error as error:
        print("Error while connecting to sqlite", record)
    finally:
        if dbConnection:
            dbConnection.close()
            print("The SQLite connection is closed")

def createTable(dbName, tableName, pkList, uniqueList, argsList)
    try:
        dbConnection = connect(dbName)
        dbCreateTableQuery = "CREATE TABLE CINEMAS (
                              CinemaNom text, Ville text PRIMARY KEY,
                              Rue text NOT NULL);"

        cursor = dbConnection.cursor()
        print("Successfully Connected to SQLite")
        cursor.execute(dbCreateTableQuery)
        dbConnection.commit()
        print("SQLite table created")

        cursor.close()

    except Error as error:
        print("Error while creating a sqlite table", error)
    finally:
        if dbConnection:
            dbConnection.close()
            print("SQLite connection is closed")

