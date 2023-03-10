import mysql.connector

connection = mysql.connector.connect(
host = "localhost",
user = "root",
password = "senha123",
database = "vehicles"

)

def show_table():
    cursor = connection.cursor()

    cursor.execute("SELECT id, brand, model, year_manufacture FROM car_info;")
    car_data = cursor.fetchall()

    cursor.close()
    connection.close()

    for car in car_data:
        print(car)