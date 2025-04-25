import sqlite3

db = sqlite3.connect("contacts.sqlite")

new_email = 'newemailupdate@update.com'
phone = input("Please enter the phone number ")
# phone = 1234

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, phone)
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?"  
# update_sql = "UPDATE contacts SET email = 'update@update.com' WHERE phone=1234"
# update_sql = "UPDATE contacts SET email = 'update@update.com'"
print(update_sql)

update_cursor = db.cursor()
# update_cursor.execute(update_sql)
# update_cursor.executescript(update_sql) will accept 2 executions and sql injection attack
update_cursor.execute(update_sql, (new_email, phone))
print("{} rows updated".format(update_cursor.rowcount))
print()
print("Are connections the same: {}". format(update_cursor.connection == db))
print()

update_cursor.connection.commit()
update_cursor.close()

# for row in db.execute("SELECT * FROM contacts"):
#     print(row)

for name, phone, email in db.execute("SELECT * FROM contacts"):
    print(name)
    print(phone)
    print(email)
    print('-' * 20)

db.close()
