import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "senha123",
    database = "vehicles"
)

cursor = connection.cursor()

sql = "INSERT INTO car_info (model, brand, year_manufacture, price) VALUES (%s, %s, %s, %s);"

data = (
    input('Insira o modelo do veículo: '),
    input('Insira a marca do veículo: '),
    input('Insira o ano de fabricação: '),
    input('Insira o preço estimado do veículo: ')
)

cursor.execute(sql, data)
connection.commit()

id = cursor.lastrowid

cursor.close()
connection.close()

print("Véiculo cadastrado. ID: ", id)