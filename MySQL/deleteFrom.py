"""
Python MySQL Delete from by

You can delete records from an existing table using the "DELETE FROM" statement

The following example deletes any record where address equals "Mountain 21"

TO NOTE:
- mydb.commit() is required to make the changes
- Without the WHERE clause in DELETE syntax, all records will be deleted
"""

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Abbeyfarm18!",
	database = "myDatabase"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

"""
Prevent SQL Injections:
It is good practice to escape the values of any query, also in delete statements.
This is to prevent sql injections, which is a common web hacking technique.

The mysql.connector module uses the placeholder %s to escape values in a delete statement
"""

sql = "DELETE FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")