from PyInquirer import prompt

from dbManagement.DBManager import *


mainMenu = [
    {
        'type'    : 'list',
        'name'    : 'userOption',
        'message' : 'Welcome to functional dependency project',
        'choices' : ["showTable", "addDF", "deleteDF","checkDF", "quit"]
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

checkDFMenu = [
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

    elif answer1.get("userOption") == "checkDF":
        answer2 = prompt(checkDFMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        dbm.getAllDF(table)
        dbm.disconnect()

    elif answer1.get("userOption") == "quit":
        return 0
        

if __name__ == '__main__':
    main()
