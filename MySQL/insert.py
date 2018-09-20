"""
Python MySQL Insert into Table

The following demonstrates how to populate a table in a database with values
"""

import mysql.connector

mydb = mysql.connector.connect (
	host = "localhost",
	user = "root",
	passwd = "",
	database = "myDatabase"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Alan", "Kildare")
mycursor.execute(sql, val)

#This line saves the changes
mydb.commit()

print(mycursor.rowcount, "record inserted.")

"""
To insert multiple values we use the executemany() method.
This takes a list of tuples to insert into the table
"""

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

mycursor.executemany(sql, val)

mydb.commit()

#Returns the total number of rows inserted
print(mycursor.rowcount, "was inserted")



"""
You can get the id of a row you just inserted by asking the cursor object
"""
print("1 record inserted, ID: ", mycursor.lastrowid)


