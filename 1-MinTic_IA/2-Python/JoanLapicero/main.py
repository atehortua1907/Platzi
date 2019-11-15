from Models.lapicero import lapicero

def run():

    while True:

        print('Fabrica tu lapicero')
        nombre = input('Digite el nombre de su lapicero: ')
        color = input('Digite el color de su lapicero: ')
        color_tinta = input('Digite el color de la tinta: ')

        objeto_lapicero = lapicero(nombre, color, color_tinta)
        objeto_lapicero.fnEscribir()



if __name__ == '__main__':
    run()
