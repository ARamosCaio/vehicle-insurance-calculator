import mysql.connector
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

cursor.execute("SELECT price FROM car_info;")
prices = cursor.fetchall()

for price in prices:
    if  < 25000:
        cursor.execute('INSERT INTO car_info (insurance_fee) VALUES (80.00)')

