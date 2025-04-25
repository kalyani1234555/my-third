import sqlite3
import datetime

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT * FROM history"):
#     utc_time = row[0]
#     # print(row)
#     local_time = datetime.datetime.now(datetime.timezone.utc).astimezone()
#     # print("{}\t{}".format(local_time, type(local_time)))
#     print("{}\t{}".format(utc_time, local_time))

for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f, histroy.time, 'localtime') AS localtime,"
                      "history.account, history.amount FROM history ORDER BY history.time"):
    print(row)

db.close()
