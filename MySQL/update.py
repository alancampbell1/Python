"""
MySQL Update Table:

You can update existing records in a table by using the UPDATE statement
"""

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Abbeyfarm18!",
	database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

"""
Again, it is considered good practice to escape values of any query. This is to prevent
SQL injections. 

The mysql.connector module uses the placeholder %s to escape values in the delete statement
"""

sql = "UPDATE customers SET address = %s WHERE address = %s"

val = ("Valley 345", "Canyon 123")

mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")