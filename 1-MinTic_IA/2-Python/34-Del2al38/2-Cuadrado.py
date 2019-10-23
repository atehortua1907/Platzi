
#por cada lado del cuadrado (4) vamos hacia adelante 50 y giramos 90 grados a la izquierda
#y asi se completa el cuadrado

import turtle

window = turtle.Screen()
david = turtle.Turtle()
david.forward(50)
david.left(90)
david.forward(50)
david.left(90)
david.forward(50)
david.left(90)
david.forward(50)
david.left(90)

turtle.mainloop()

#Ejemplo enviado por un compañero del curso, pinta un exagono 360 veces y 
#se ve en forma de espiral
# window = turtle.Screen()

# colors=['red','purple','blue','green','yellow','orange']

# t = turtle.Pen()
# t.speed(0)
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x/100+1)
#     t.forward(x)
#     t.left(59)

# turtle.mainloop()
