"""
MySQL Join

You can combine rows from two or more tables, based on a related column by using a
JOIN statement.

Two tables can be combined using their columns
"""

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "Abbeyfarm18!",
	database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT \
		users.name AS user, \
		products.name AS favourite	\
		FROM users \
		INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
	print(x)


"""
Alternatively, you can use left and right joins depending on what information you
want to show
"""
sql = "SELECT \
		users.name AS user, \
		products.name AS favourite	\
		FROM users \
		RIGHT JOIN products ON users.fav = products.id"

sql = "SELECT \
		users.name AS user, \
		products.name AS favourite	\
		FROM users \
		LEFT JOIN products ON users.fav = products.id"




