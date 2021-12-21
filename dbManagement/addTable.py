from sqlite3 import *

try: 
    dbConnection = connect('DATABANANA')
    dbQuery = '''CREATE TABLE SNCB (
                Tel TEXT PRIMARY KEY,
                Ville TEXT NOT NULL);'''

    cursor = dbConnection.cursor()

    cursor.execute(dbQuery)
    cursor.execute('''INSERT INTO SNCB VALUES ("0478199487", "Blaton")''')
    dbConnection.commit()

    cursor.close()

except Error as error:
    print("Error while creating SQLite Table" , error)
finally:
    if dbConnection:
        dbConnection.close()
