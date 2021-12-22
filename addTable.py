from sqlite3 import *

try: 
    dbConnection = connect('DATABANANA')
    dbQuery = '''CREATE TABLE SNCB (
                CinemaNom TEXT NOT NULL,
                Rue TEXT NOT NULL,
                Ville TEXT NOT NULL,
                Telephone TEXT NOT NULL,
                Titre TEXT NOT NULL,
                Regisseur TEXT NOT NULL,
                Duree TEXT NOT NULL,
                Heure TEXT NOT NULL);'''

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
