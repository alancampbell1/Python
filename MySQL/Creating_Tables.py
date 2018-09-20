"""
Python mySQL Create Table

To create a table in a database we use the CREATE TABLE statement.
It is important we define the name of the database before we create our table.
"""

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "",
	database = "myDatabase"
)

mycursor = mydb.cursor()

#Our table, customers will have two columns, name and address. Both with a length of 255
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


#Again, to make sure everything worked ok, we can use the SHOW TABLES function

mycursor = mydb.cursor()
mycursor.execute("SHOW TABLES")

for x in mycursor:
	print(x)


"""
When creating a table, you should also create a column with a unique key for each record.
AKA a primary key.
INT AUTO_INCREMENT PRIMARY KEY will insert a new number for each record.
"""

mycursor.execute("CREATE TABLE customers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")

#To add a Primary key to an already existing table we do the following
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")



