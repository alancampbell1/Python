"""
Python MySQL Order By

Python allows you to Sort the result in ascending or descending order. The ORDER BY keyword
does this for us.
"""

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Abbeyfarm18!",
	database = "mydatabase"
)

mycursor = mydb.cursor()

#orders the list in alphabetical order
sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)


#orders the list in descending order
sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)

