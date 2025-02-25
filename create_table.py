import sqlite3
    
con = sqlite3.connect("login.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE users(
username VARCHAR(20) NOT NULL PRIMARY KEY,
password VARCHAR(20) NOT NULL)
    """)
print("Table created successfully")