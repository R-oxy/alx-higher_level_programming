#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states
table of `hbtn_0e_0_usa` where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: {} <mysql_username> <mysql_password> <database_name> <state_name>".format(sys.argv[0]))
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                             passwd=mysql_password, db=database_name)
        cursor = db.cursor()

        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
        cursor.execute(query, (state_name,))

        for row in cursor.fetchall():
            print(row)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
        sys.exit(1)
