from PyInquirer import prompt, Separator

from dbManagement.DBManager import *


mainMenu = [
    {
        'type'    : 'list',
        'name'    : 'userOption',
        'message' : 'Welcome to functional dependency project',
        'choices' : ["getTables", "showTable", Separator(), "addDF", "deleteDF","getAllDF", Separator(), "quit"]
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

getTablesMenu = [
    {
        'type'    : 'input',
        'name'    : 'db',
        'message' : 'Enter the data base name'
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
        for data in dbm.getTable(table):
            print(data, '\n')
        dbm.disconnect()

    elif answer1.get("userOption") == "addDF":
        answer2 = prompt(DFMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        lhs     = answer2.get("lhs")
        rhs     = answer2.get("rhs")
        dbm     = DBManager(db)
        dbm.addDF(table, lhs, rhs)
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

    elif answer1.get("userOption") == "getAllDF":
        answer2 = prompt(showTableMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        dbm.displayDF(table)
        dbm.disconnect()

    elif answer1.get("userOption") == "getTables":
        answer2 = prompt(getTablesMenu)
        db      = answer2.get("db")
        dbm     = DBManager(db)
        dbm.displayAllTables()
        dbm.disconnect()

    elif answer1.get("userOption") == "quit":
        return 0
        

if __name__ == '__main__':
    main()
