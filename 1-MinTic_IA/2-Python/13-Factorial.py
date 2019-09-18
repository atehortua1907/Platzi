def factorial(number):
    if(number == 0): #caso base
        return 1
    
    return number * factorial(number -1); 

if(__name__ == '__main__'):
    print(factorial(int(input('Escribe un número: '))))