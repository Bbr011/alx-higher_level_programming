#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa sorted in ascending order by
states.id
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = conn.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    states = c.fetchall()
    for s in states:
        print(s)
    c.close()
    db.close()
