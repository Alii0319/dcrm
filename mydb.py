import MySQLdb

database = MySQLdb.connect(
    host='localhost',
    user='root',
    passwd='12345@Pak'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print('done')
