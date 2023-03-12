def validate_year():
    year_manufacture = int(input('Insira o ano do veículo: '))
    if year_manufacture in range(1970, 2023):
        return year_manufacture
    print('Apenas valores entre 1970 e 2023')
    return validate_year()


def validate_brand():
    brand = input('Insira a marca do veículo: ')
    brands = ['Volkswagen', 'Chevrolet', 'Fiat', 'Toyota', 'Kia', 'Renault', 'Hyundai', 'Ford', 'Honda', "Citroën", 'Peugeot']
    if brand in brands:
        return brands[brands.index(brand)]
    print('Marca inválida')
    print(*brands, sep=", ")
    return validate_brand()