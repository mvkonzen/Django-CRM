import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Marcus$86',

)

cursorObjetc = dataBase.cursor()

cursorObjetc.execute('CREATE DATABASE Inspira')

print('All Done!')
