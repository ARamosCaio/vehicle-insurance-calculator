import mysql.connector

connection = mysql.connector.connect(
host = "localhost",
user = "root",
password = "senha123",
database = "vehicles"

)

def show_cars_table():
    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT id, model, brand, price FROM car_info;")
    car_data = cursor.fetchall()

    cursor.close()
    connection.close()

    for car in car_data:
        print(car["id"], car["model"], car["brand"], car["price"])

