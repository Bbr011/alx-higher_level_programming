#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    c = db.cursor()
    c.execute("""SELECT cities.name FROM cities 
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC""",(argv[4], ))
    print(", ".join(map(lambda x: x[0], c.fetchall())))
    c.close()
    db.close()
