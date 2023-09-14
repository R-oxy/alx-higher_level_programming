#!/usr/bin/python3
"""
script that lists all states with a name starting with N
(upper N) from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <mysql_username> <mysql_password> <database_name>"
              .format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                             passwd=mysql_password, db=database_name)
        cursor = db.cursor()
        cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC;"
        )

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
        sys.exit(1)
