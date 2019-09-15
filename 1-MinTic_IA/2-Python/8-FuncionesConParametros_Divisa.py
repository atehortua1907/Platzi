def run():
    print('C A L C U L A D O R A')
    print('Convierta pesos mexicanos a pesos colombianos')
    print('')

    amount = float(input('Ingresa la cantidad de pesos mexicanos a convertir'))

    result = foreign_exchange_calculator(amount)

    print('${} pesos mexicanos son ${} pesos colombianos'.format(amount, result))

def foreign_exchange_calculator(amount):
    mex_to_col_rate = 145.97
    return mex_to_col_rate * amount

if __name__=='__main__':
    run()

