
from random import *
from turtle import *
 
#Configuramos la pantalla
pantalla = Screen()
pantalla.bgcolor("purple")

 #Dibujamos los recuadros
def Square(x, y):
    up()
    goto(x, y)
    down()
    color('black', 'pink')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

 #parametros para los numeros 
def Numbering(x, y):
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)
 
 #cordenadas de separacion de los recuadros 
def Coordinates(count):
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

 #Manipulacion de clicks en la pantalla
def click(x, y):
    spot = Numbering(x, y)
    marco = state ['marco']
 
    if marco is None or marco == spot or tiles[marco] != tiles[spot]:
        state['marco'] = spot
    else:
        hide[spot] = False
        hide[marco] = False
        state['marco'] = None
 
 
 #Dibujar tablero
def draw():
    clear()
    goto(0, 0)
    stamp()

 # declarar el numero de recuadros 
    for count in range(32):
        if hide[count]:
            x, y = Coordinates(count)
            Square(x, y)
 
    marco = state['marco']
 
    if marco is not None and hide[marco]:
        x, y = Coordinates(marco)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[marco], font=('ITALIC', 30, 'normal'))
 
    update()
    ontimer(draw, 10)
 

 #Estado del juego
tiles = list(range(16)) * 2
state = {'marco': None}
hide = [True] * 32

shuffle(tiles)
tracer(False)
onscreenclick(click)
draw()
done()