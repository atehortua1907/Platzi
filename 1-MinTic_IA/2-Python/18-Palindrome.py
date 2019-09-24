if __name__ == "__main__":
    isPalindrome = False
    while not isPalindrome:
        palabra = input('Ingrese una palabra palíndroma: ')
        isPalindrome = palabra == palabra[::-1]
        if isPalindrome:
            print('La palabra {} es palíndrome'.format(palabra))
        else:
            print('La palabra {} no es palíndrome'.format(palabra))