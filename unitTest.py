import unittest
from dbManagement.DBManager import *

class TestDBManagerMethods(unittest.TestCase):

    def test_addDF(self):
        """This also test getAllDF() method"""
        dbm = DBManager("DATABANANA")
        dbm.addDF("TestTable", "Testlhs1 Testlhs2", "Testrhs")
        self.assertTrue(("TestTable", "Testlhs1 Testlhs2", "Testrhs") in dbm.getAllDF("TestTable"))
        dbm.disconnect()

    def test_deleteDF(self):
        dbm = DBManager("DATABANANA")
        dbm.deleteDF("TestTable", "Testlhs1 Testlhs2", "Testrhs")
        self.assertFalse(("TestTable", "Testlhs1 Testlhs2", "Testrhs") in dbm.showTable("FuncDep"))
        dbm.disconnect()


if __name__ == '__main__':
    unittest.main()
