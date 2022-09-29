import sqlite3

conn = sqlite3.connect('users.db')
print("Opened database successfully")

conn.execute('CREATE TABLE users (fname TEXT, lname TEXT, email TEXT, password TEXT)')
print("Table created successfully")
conn.close()