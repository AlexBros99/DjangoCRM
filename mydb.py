import mysql.connector 


dataBase=mysql.connector.connect(
    host='localhost',
    user = 'root',
    passwd = 'Polska99',
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmholder")

print("Done")