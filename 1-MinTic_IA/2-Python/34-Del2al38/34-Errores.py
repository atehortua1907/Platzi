countries = {
    'mexico': 122,
    'colombia': 49,
    'argentina': 43,
    'chile': 18,
    'peru':31
}

while True:
    country = str(input("Escribe el nombre de un país: ")).lower()
    #aquí se puede generar un error al verificar que la llave no existe
    try:
        print(f'La población de {country} es de {countries[country]} millones')
    except KeyError:
        print(f'No tenemos el dato de la población de {country}...')
    #Se maneja el error con un mensaje personalizado (KeyError)