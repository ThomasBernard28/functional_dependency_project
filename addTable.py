from sqlite3 import *

try: 
    dbConnection = connect('DATABANANA')
    dbQuery = '''CREATE TABLE TEST2 (
                A TEXT NOT NULL,
                B TEXT NOT NULL,
                C TEXT NOT NULL,
                D TEXT NOT NULL,
                E TEXT NOT NULL,
                F TEXT NOT NULL,
                G TEXT NOT NULL,
                H TEXT NOT NULL);'''

    cursor = dbConnection.cursor()

    cursor.execute(dbQuery)
    cursor.execute('''INSERT INTO SNCB VALUES ("Utopia", "6 Rue du parc", "Alost", "053 66 33 33", "Felice", "P. Delpeut", "1:39", "19:15")''')
    dbConnection.commit()

    cursor.close()

except Error as error:
    print("Error while creating SQLite Table" , error)
finally:
    if dbConnection:
        dbConnection.close()
