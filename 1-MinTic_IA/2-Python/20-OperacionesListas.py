#List Slices
#Las listas, al igual que los strings, pueden "rebanarse".

lista = [1,2,3,4,5,6]
lista[1:] #[2,3,4,5,6]
lista[1:3]#[2,3] de 1 a 3 (sin incluirse)
lista[1:6:2]#[2,4,6] de 1 a 6 de dos en dos
lista[::-1]#[6,5,4,3,2,1]

#Modificaciones en la lista
mi_lista = ['juan','pedro','pepe']
mi_lista[0] = 'laura' #['laura','pedro','pepe']
mi_lista.append('estela') #['laura','pedro','pepe', 'estela']
nombre = mi_lista.pop() #['laura','pedro','pepe']
nombre == 'estela' #True

mi_otra_lista = [4,3,7,1]
mi_otra_lista.sort() #[1,3,4,7]
mi_lista.extend(mi_otra_lista) #['juan','pedro','pepe',4,3,7,1]
del mi_otra_lista[0] #[3,7,1]

casa = 'casa'
type(casa) #<type 'str'>
lista_casa = list(casa)#['c','a','s','a']
str_casa = ''.join(lista_casa) #'casa'

