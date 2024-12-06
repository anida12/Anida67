import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",    
    password=""
)

if mydb.is_connected():
    print("Berhasil Terhubung ke Database")