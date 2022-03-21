import turtle
t=turtle.Pen()
turtle.bgcolor("black")
colores=['red', 'yellow', 'blue', 'green', 'orange', 'purple', 'white', 'gray', 'brown', 'aqua']
nombre = turtle.textinput("Nombre", "Cual es tu nombre?")
repeticiones = int(turtle.numinput("Repeticiones", "cuantas repeticiones(1-10)?", 5, 1, 10) )
for x in range(100):
    t.pencolor(colores[x%repeticiones%10])
    t.penup()
    t.forward(x*4)
    t.pendown()
    t.write(nombre, font=("Arial", int( (x*2 + 4) / 4), "bold") )
    t.left(180/repeticiones+2)