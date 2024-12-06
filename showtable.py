import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",    
    database="db_penjualan"
)

mycursor = mydb.cursor()
mycursor.execute('DESCRIBE kategori')
for x in mycursor:
    print(x)