from PyInquirer import prompt

from dbManagement.DBManager import *


mainMenu = [
    {
        'type'    : 'list',
        'name'    : 'userOption',
        'message' : 'Welcome to functional dependency project',
        'choices' : ["showTable", "example", "quit"]
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

def main():
    answer1 = prompt(mainMenu)

    if answer1.get("userOption") == "showTable":
        answer2   = prompt(showTableMenu)
        db        = answer2.get("db")
        table     = answer2.get("table")
        dbm       = DBManager(db)
        for data in dbm.showtable(table):
            print(data, '\n')
        dbm.disconnect()

    elif answer1.get("userOption") == "quit":
        return 0

    elif answer1.get("userOption") == "example":
        print("This is an example.")
        

if __name__ == '__main__':
    main()
