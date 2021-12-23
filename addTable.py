from sqlite3 import *

try: 
    dbConnection = connect('DATABANANA')
    dbQuery = '''CREATE TABLE TEST3(
                A TEXT NOT NULL,
                B TEXT NOT NULL,
                C TEXT NOT NULL);'''

    cursor = dbConnection.cursor()

    cursor.execute(dbQuery)
    dbConnection.commit()

    cursor.close()

except Error as error:
    print("Error while creating SQLite Table" , error)
finally:
    if dbConnection:
        dbConnection.close()
