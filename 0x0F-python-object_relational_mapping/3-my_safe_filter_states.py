#!/usr/bin/python3
"""
script that is safe from MySQL injections
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state>"
              .format(sys.argv[0]))
        sys.exit(1)

    username, password, database, state = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    cursor.execute(query, (state,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
