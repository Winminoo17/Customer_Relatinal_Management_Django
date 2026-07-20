import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = 'root',
    password = '!wmo!26211317pw',
)

cursorObject = mydb.cursor()

cursorObject.execute(
    "CREATE DATABASE dcrm_db"
)

print("Database created successfully")