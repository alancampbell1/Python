"""
Python MySQL WHERE

When selecting records from a table, you can filter the selection by using 'WHERE'
"""

import mysql.connector

mydb = mysql.connector.connect (
	host = "localhost",
	user = "root",
	passwd = "",
	database = "myDatabase"
)

mycursor = mydb.cursor()

#returns all the rows from table customers where the address column is equal to Park Lane 38
sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)

"""
Wildcard Characters
You can also make sections on records that start, include or end with a given letter
We use the % to represent this
"""

#Returns all columns where address has the word 'way' in it
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
	print(x)


"""
Prevent SQL Injections
When query values are provided by the user, you should escape the values.
This is to prevent SQL injections, a common web hacking technique

The mysql.connector module has methods to escape query values

"""

#Escape query values by using the placeholder %s method
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
	print(x)

