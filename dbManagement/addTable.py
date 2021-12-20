from sqlite3 import *
from dbFunctions import *

try:
    dbConnection = connect('DATABANANA')
    dbCreateTableQuery =  '''CREATE TABLE SNCB (
                           CinemaNom TEXT NOT NULL,
                           Rue TEXT NOT NULL,
                           Ville TEXT NOT NULL,
                           Téléphone INTEGER NOT NULL,
                           Titre TEXT NOT NULL,
                           Régisseur TEXT NOT NULL,
                           Durée INTEGER NOT NULL,
                           Heure INTEGER NOT NULL);'''


