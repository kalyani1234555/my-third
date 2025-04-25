import sqlite3

# db = sqlite3.connect("contacts.sqlite")
#
# cursor = db.cursor()
# cursor.execute("SELECT * FROM contacts")
#
# print(cursor.fetchall())
#
# db.close()

conn = sqlite3.connect("contacts.sqlite")

name = input("Please enter a name to search for ")

# for row in conn.execute("SELECT * FROM contacts WHERE name = ?", (name,)):
for row in conn.execute("SELECT * FROM contacts WHERE name Like ?", (name,)):

    print(row)

conn.close()
