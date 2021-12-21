from PyInquirer import prompt

from dbManagement.DBManager import *


mainMenu = [
    {
        'type'    : 'list',
        'name'    : 'userOption',
        'message' : 'Welcome to functional dependency project',
        'choices' : ["showTable", "addDF", "deleteDF", "quit"]
    }
]

showTableMenu = [
    {
        'type'    : 'input',
        'name'    : 'db',
        'message' : 'Enter the data base name'
    },

    {
        'type'    : 'input',
        'name'    : 'table',
        'message' : 'Enter the table name'
    }
]

DFMenu = [
    {
        'type'    : 'input',
        'name'    : 'db',
        'message' : 'Enter the data base name'
    },

    {
        'type'    : 'input',
        'name'    : 'dftable',
        'message' : 'Enter the DF table name'
    },

    {
        'type'    : 'input',
        'name'    : 'table',
        'message' : 'Enter table name'
    },

    {
        'type'    : 'input',
        'name'    : 'lhs',
        'message' : 'Enter lhs'
    },

    {
        'type'    : 'input',
        'name'    : 'rhs',
        'message' : 'Enter rhs'
    }
]

def main():
    answer1 = prompt(mainMenu)

    if answer1.get("userOption") == "showTable":
        answer2 = prompt(showTableMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        for data in dbm.showTable(table):
            print(data, '\n')
        dbm.disconnect()

    elif answer1.get("userOption") == "addDF":
        answer2 = prompt(DFMenu)
        db      = answer2.get("db")
        dfTable = answer2.get("dftable")
        table   = answer2.get("table")
        lhs     = answer2.get("lhs")
        rhs     = answer2.get("rhs")
        dbm     = DBManager(db)
        dbm.addDF(dfTable, table, lhs, rhs)
        dbm.disconnect()

    elif answer1.get("userOption") == "deleteDF":
        answer2 = prompt(DFMenu)  
        db      = answer2.get("db")
        table   = answer2.get("table")
        lhs     = answer2.get("lhs")
        rhs     = answer2.get("rhs")
        dbm     = DBManager(db)
        dbm.deleteDF(table, lhs, rhs)
        dbm.disconnect()

    elif answer1.get("userOption") == "quit":
        return 0
        

if __name__ == '__main__':
    main()
