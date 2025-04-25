import sqlite3
import datetime
import pytz
import pickle

db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)


# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f, histroy.time, 'localtime') AS localtime,"
#                       "history.account, history.amount FROM history ORDER BY history.time"):
#     print(row)

for row in db.execute("SELECT * FROM history"):
    utc_time = row[0]

    zone = pickle.loads(picked_zone)
    # zone = pytz.timezone('CET')
    # zone = pytz.timezone('Australia/Adelaide')
    local_time = datetime.datetime.now(datetime.timezone.utc).astimezone(zone)
    print("{}\t{}\t{}".format(utc_time, local_time, local_time.tzinfo))


db.close()
