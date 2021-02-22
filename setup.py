import sqlite3

conn = sqlite3.connect('reviewData.db')
print ("Opened database successfully")

conn.execute('CREATE TABLE reviews (Username TEXT, Restaurant TEXT, Food REAL, Service REAL, Ambience REAL, Price REAL, Overall REAL, Review TEXT)')
print ("Table created successfully")
conn.close()