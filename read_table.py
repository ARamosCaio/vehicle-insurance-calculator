import mysql.connector

connection = mysql.connector.connect(
host = "localhost",
user = "root",
password = "senha123",
database = "vehicles"

)

def show_cars_table():
    cursor = connection.cursor()

    cursor.execute("SELECT id, model, brand, price FROM car_info;")
    car_data = cursor.fetchall()

    cursor.close()
    connection.close()

    for car in car_data:
        print(car[0], car[1], car[2], car[3])

