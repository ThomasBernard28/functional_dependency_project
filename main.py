import click
from PyInquirer import prompt
from prompt_toolkit.validation import Validator, ValidationError

from dbManagement.DBManager import *


@click.group()
def main():
    """
    DB project 2021-2022.\n\n
    thomas.BERNARD@student.umons.ac.be - theo.GODIN@student.umons.ac.be
    """


@main.command("showtable")
@click.option("--db")
@click.option("--table")
def showtable(db, table):
    dbm = DBManager(db)
    dbm.showTable(table)
    dbm.disconnect()


if __name__ == '__main__':
    main()
