#!/usr/bin/python3
""" lists all states with a name starting with N"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    query = """SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    c.execute(query)
    for s in c.fetchall():
        print(s)
    c.close()
    db.close()

