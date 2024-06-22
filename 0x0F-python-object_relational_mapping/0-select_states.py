#!/usr/bin/python3
# script that list all the states databases of hbtn_0e_0_usa.
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    for s in c.fetchall():
        print(s)
