#!/usr/bin/python3
"""
Lists all states with a name starting with N (upper N)
It takes 3 arguments: mysql username, mysql password and database name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.con
