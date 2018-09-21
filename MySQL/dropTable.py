"""
Drop Table

You can delete an existing table by using the 'DROP TABLE' statement

IF EXISTS is an optional extra to avoid errors being thrown to the screen
"""

import mysql.connector

mydb = mysql.connector.connect(
	host = "localhost",
	user = "root",
	passwd = "AAbbeyfarm18!",
	database = "mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE IF EXISTS customers2"

mycursor.execute(sql)