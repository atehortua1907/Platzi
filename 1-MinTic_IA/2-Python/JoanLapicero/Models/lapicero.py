#definir clase
class lapicero:

    #definir constructor
    def __init__(self, nombre, color, color_tinta):
        self.nombre = nombre
        self.color = color 
        self.color_tinta = color_tinta

    #definir función
    def fnEscribir(self):
        self.estado = f'''
        **** 
         Estoy escribiendo .../../.../ con el lapicero {self.nombre}
          con tinta de color {self.color_tinta} 
        ****
         '''
        print(self.estado)
