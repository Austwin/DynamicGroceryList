import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = 'austin',
    passwd = 'Halo767900!!'
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE DynamicGroceryList")

print("All done")