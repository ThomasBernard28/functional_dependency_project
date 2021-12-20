from sqlite3 import *
#Code from https://pynative.com/python-sqlite/
def connection(dbName):
    try:
        
        dbConnection = connect(dbName)
        cursor = dbConnection.cursor()

        return dbConnection , cursor

    except Error as error:
        print("Error while connecting to sqlite")


def deconnection():
    cursor.close()
    dbConnection.close()
        
def readSqliteTable():
    dbConnection(dbName)
    try:
        dbSelectQuery = """SELECT * SNCB"""
        cursor.execute(dbSelectQuery)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("CinemaNom ", row[0])
            print("Rue: ", row[1])
            print("Ville: ", row[2])
            print("Téléphonne: ", row[3])
            print("Titre: ", row[4])
            print("")
            print("\n")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

readSqliteTable()
