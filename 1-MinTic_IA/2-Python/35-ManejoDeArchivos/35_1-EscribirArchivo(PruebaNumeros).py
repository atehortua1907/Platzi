import os.path

save_path = 'D:/Repositories/Platzi/1-MinTic_IA/2-Python/35-ManejoDeArchivos/'
fileName = 'numeros'
completeName = os.path.join(save_path, f"{fileName}.txt")

def run():
    with open(completeName,'w') as archivo:
        for i in range(10):
            archivo.write(str(i))
    
    #sin context manager (with open()...)
    # try:
    #     archivo = open('numeros.txt','w')
    # finally:
    #     archivo.close

if __name__ == '__main__':
    run()

    