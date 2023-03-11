import mysql.connector

def register_car():
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

    record_id = cursor.lastrowid

    cursor.close()
    connection.close()

    return("Veículo cadastrado. ID: ", record_id)