from PyInquirer import prompt, Separator

from dbManagement.DBManager import *


mainMenu = [
    {
        'type'    : 'list',
        'name'    : 'userOption',
        'message' : 'Welcome to functional dependency project',
        'choices' : ["get table form",Separator(),"get all tables name", "show one table", Separator(), "add a DF", "delete a DF","delete all DF of a table" ,"get all DF of a table", Separator(), "search keys", Separator(), "quit"]
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

    if answer1.get("userOption") == "show one table":
        """ show one table """
        answer2 = prompt(showTableMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        for data in dbm.getTable(table):
            print(data, '\n')
        dbm.disconnect()

    elif answer1.get("userOption") == "get table form":
        """ Return the form of the table"""
        answer2 = prompt(showTableMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        dbm.getForm(table)
        dbm.disconnect()

    elif answer1.get("userOption") == "add a DF":
        """" add a df """
        answer2 = prompt(DFMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        lhs     = answer2.get("lhs")
        rhs     = answer2.get("rhs")
        dbm     = DBManager(db)
        dbm.addDF(table, lhs, rhs)
        dbm.disconnect()

    elif answer1.get("userOption") == "delete a DF":
        """ delete a df """
        answer2 = prompt(DFMenu)  
        db      = answer2.get("db")
        table   = answer2.get("table")
        lhs     = answer2.get("lhs")
        rhs     = answer2.get("rhs")
        dbm     = DBManager(db)
        dbm.deleteDF(table, lhs, rhs)
        dbm.disconnect()

    elif answer1.get("userOption") == "get all DF of a table":
        """ get all df of a table """
        answer2 = prompt(showTableMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        result  = 0
        DFList  = dbm.getAllDF(table)
        for DF in DFList:
            if DF[0] == table:
                if not result:
                    result = "Here are all the DF(s) of the "+DFList[0][0]+ " table :\n"
                result += DF[1] + " -----> " + DF[2] + "\n"
        if not result:
            result = "No DF found for " + table
        print(result)
        dbm.disconnect()

    elif answer1.get("userOption") == "delete all DF of a table":
        """delete all df of a table"""
        answer2 = prompt(showTableMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        dbm.deleteAllDF(table)
        dbm.disconnect()

    elif answer1.get("userOption") == "get all tables name":
        """ get all tables name """
        answer2 = prompt(getTablesMenu)
        db      = answer2.get("db")
        dbm     = DBManager(db)
        for t in dbm.getAllTables():
            print("> " + t)
        dbm.disconnect()

    elif answer1.get("userOption") == "search keys":
        """ search keys of a table """
        answer2 = prompt(showTableMenu)
        db      = answer2.get("db")
        table   = answer2.get("table")
        dbm     = DBManager(db)
        print("The candidate key is :",str(dbm.displayKeys(table)))
        dbm.disconnect()

    elif answer1.get("userOption") == "quit":
        """ quit """
        return 0
        

if __name__ == '__main__':
    main()
