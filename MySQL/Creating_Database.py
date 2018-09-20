"""
Creating a database in mySQL using Python

To do so, you need the 'CREATE DATABASE' statement.
- The mysql.connector is imported to carry out the necessary functions.
- The connection to mySQL is made using the correct credentials.
- A Database entitled myDatabase is created using the CREATE DATABASE function.
- SHOW DATABASES function is used to make sure the database has been created.
- A for loop prints each database accordingly.

"""

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE myDatabase")

mycursor.execute("SHOW DATABASES")

for x in mycursor:
	print(x)