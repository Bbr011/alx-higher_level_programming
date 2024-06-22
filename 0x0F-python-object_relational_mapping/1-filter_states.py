#!/usr/bin/python3
""" lists all states with a name starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id ASC")
    for s in c.fetchall():
        if s[0].startswith("N"):
            print(s)
    c.close()
    db.close()
