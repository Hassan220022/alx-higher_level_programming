#!/usr/bin/python3
"""
A script that lists all states from the database `hbtn_0e_0_usa`.
This script takes 3 arguments: mysql username, password, and database name.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]  # The MySQL username
    mysql_password = sys.argv[2]  # The MySQL password
    database_name = sys.argv[3]   # The database name

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=mysql_username, passwd=mysql_password, db=database_name)

    # Create a cursor object
    cur = db.cursor()

    # Execute the SQL query
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of lists.
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()
