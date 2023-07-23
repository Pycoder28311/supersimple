import mysql.connector

dataBase = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    passwd = 'brogrammer12',

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco1")

print('all ok1')