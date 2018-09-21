"""
MySQL Limit:

You can limit the number of records returned from the query using the "LIMIT" statement
"""

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Abbeyfarm18!",
	database = "myDatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)

"""
If you want to return 5 records, starting from the 3rd record, you can use the 
"OFFSET" keyword
"""

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
	print(x)