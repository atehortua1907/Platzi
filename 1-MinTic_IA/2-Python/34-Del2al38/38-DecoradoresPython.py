def protected(func):

    def wrapper(password):
        if password == 'platzi':
            return func()
        else:
            print('La contraseña es incorrecta')
    
    return wrapper

@protected #Esta función seria el parametro que recibe la función protected
def protected_func():
    print('Tu contraseña es correcta')

if __name__ == '__main__':
    password = str(input('Ingresa tu contraseña: '))
    protected_func(password)