#!/usr/bin/python3
"""script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument v2"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2], db=argv[3], charset="uft8")
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = %s ORDER BY states.id ASC", (argv[4], ))
    for s in c.fetchall():
        print(s)
    c.close()
    db.close()
