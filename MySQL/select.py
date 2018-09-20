"""
Python MySQL Select from

How to query data from a table in database using Python
"""

import mysql.connector

mydb = mysql.connector.connect (
	host = "localhost",
	user = "root",
	passwd = "",
	database = "myDatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

#fetchall() fetches all the rows from the last executed statement
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#To select only specific columns

mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#If you are only interested in one row, you can use the fetchone() method
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

