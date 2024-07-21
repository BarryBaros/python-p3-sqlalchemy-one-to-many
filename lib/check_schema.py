# check_schema.py
import sqlite3

conn = sqlite3.connect('one_to_many.db')
cursor = conn.cursor()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

print("Tables in the database:", tables)

conn.close()
