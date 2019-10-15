from moduloLamp import Lampara #Del modulo "moduloLamp" importate la clase "Lampara"
from moduloLamp import Foco #Del modulo "moduloLamp" importate la clase "Foco"

def run():
    lamp = Lampara(is_turned_on = True)

    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [p]render
            [a]pagar
            [s]alir
        '''))

        if command == 'p':
            lamp.turn_on()
        elif command == 'a':
            lamp.turn_off()
        else:
            break

if __name__ == '__main__':
    run()