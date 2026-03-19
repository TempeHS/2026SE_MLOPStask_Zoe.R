import sqlite3 as sql

connection = sql.connect("databaseFiles/database.db")
cursor = connection.cursor()
