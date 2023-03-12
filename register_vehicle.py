import mysql.connector
import validate

#def register_car():
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
    validate.validate_brand(),
    validate.validate_year(),
    input('Insira o preço estimado do veículo: ')
)

cursor.execute(sql, data)
connection.commit()

record_id = cursor.lastrowid

cursor.close()
connection.close()

("Veículo cadastrado. ID: ", record_id)