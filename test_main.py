import pytest
from dbManagement.DBManager import *

def test_addDF():
    """This also test getAllDF() method"""
    dbm = DBManager("DATABANANA")
    dbm.addDF("TestTable", "Testlhs1 Testlhs2", "Testrhs")
    assert ("TestTable", "Testlhs1 Testlhs2", "Testrhs") in dbm.getAllDF("TestTable")
    dbm.disconnect()

def test_deleteDF():
    dbm = DBManager("DATABANANA")
    dbm.deleteDF("TestTable", "Testlhs1 Testlhs2", "Testrhs")
    assert not ("TestTable", "Testlhs1 Testlhs2", "Testrhs") in dbm.getTable("FuncDep")
    dbm.disconnect()
