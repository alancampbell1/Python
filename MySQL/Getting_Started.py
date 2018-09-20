"""
Python mySQL

Python can be used in database applications, similar to PHP.
One of the most popular databases is mySQL

In order to access the mySQL database Python needs a mySQL driver.
This is done by using PIP to install "MySQL Connector"

From here you need to import it into each Python document using the 
command below
"""




import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
)




print(mydb)