import mysql.connector
import read_table
import os

os.system('cls')

print('\nVehicle Insurance Calculator\n')

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "senha123",
    database = "vehicles"
)

cursor = connection.cursor()

cursor.execute("SELECT id, price FROM car_info;")
prices = cursor.fetchall()


sql = ('UPDATE car_info SET insurance_fee = %s WHERE id = %s;')
for price in prices:
    if price[1] < 20000:
        data = (80.00, price[0])

    elif price[1] in range(20000, 30000):
        data = (120.00, price[0])

    elif price[1] in range(30000, 45000):
        data = (155.00, price[0])

    elif price[1] in range(45000, 65000):
        data = (210.00, price[0])

    elif price[1] in range(65000, 90000):
        data = (275.00, price[0])

    elif price[1] in range(90000, 120000):
        data = (375.00, price[0])

    elif price[1] in range(120000, 175000):
        data = (515.00, price[0])

    elif price[1] in range(175000, 250000):
        data = (725.00, price[0])

    cursor.execute(sql, data)
connection.commit()


    


