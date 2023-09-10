'''In this file I will be showing how to how to connect the database using..

We have first created a connector to connect to the dabatabse and then used my cursor as an object to
create the table'''

import mysql.connector
db = mysql.connector.connect(
    host = "localhost"
    user = "root"
    passwd ="root"
    database ="testdatabase"
)

mycursor = db.cursor()
mycursor.execute("CREATE TABLE Person (Id INT PRIMARY KEY, Name VARCHAR(50, Age INT NOT NULL, Address VARCHAR(50)")
mycursor.execute("INSERT INTO Person (name,age) VALUES ('Sagar',32)")