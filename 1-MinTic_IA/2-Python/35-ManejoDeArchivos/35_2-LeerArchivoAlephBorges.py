import os.path

path = 'D:/Repositories/Platzi/1-MinTic_IA/2-Python/35-ManejoDeArchivos/'
fileName = 'aleph'
completeName = os.path.join(path,f"{fileName}.txt")

def run():

    with open(completeName, encoding="utf8") as archivo:
        # print(archivo.readlines()) #readlines() crea una lista con cada una de las lineas del archivo
        counter = 0
        for line in archivo:
            counter += line.count('Beatriz')
        
        print(f"La palabra Beatriz se encuentra {counter} veces")

if __name__ == '__main__':
    run()