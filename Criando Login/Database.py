import sqlite3

connection = sqlite3.connect('UsersData.db')
cursor = connection.cursor()
cursor.execute(""" Create table if not exists Users (
               id integer not null primary key autoincrement,
               username varchar(50),
               password varchar(25)
               
);""")

cursor.execute( """ INSERT INTO Users (username,password) VALUES("Joaquim","789535");""")
cursor.execute( """ INSERT INTO Users (username,password) VALUES("Julia","123456");""")
cursor.execute( """ INSERT INTO Users (username,password) VALUES("Amanda","654321");""")
