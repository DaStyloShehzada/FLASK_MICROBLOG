import sqlite3

connection = sqlite3.connect('data.db')
cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS MICROBLOG (ID INTEGER PRIMARY KEY,DATA TEXT)"
cursor.execute(create_table)
