"""Paint, for drawing shapes.

Exercises

1. Add a color.
2. Complete circle.
3. Complete rectangle.
4. Complete triangle.
5. Add width parameter.
"""

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start, end):
    """Draw circle from start to end."""
    pass  # TODO


def rectangle(start, end):
    """Draw rectangle from start to end."""
    pass  # TODO
    up()
    goto(start.x, start.y)  
    down()                 #De la linea 31 a 33 hace que la tortuga vaya a la posición que le indiquemos
    begin_fill()           #Inicia el dibujo   

    for count in range(2): #For para realizar el proceso 2 veces
        forward(end.x - start.x)  #Avanza la distancia de valor x
        right(90)                 #Gira 90 grados a la derecha
        forward((end.x - start.x)/2) #Avanza la distancia de valor x pero se acorta para que sea el lado menor
        right(90)                 #Gira 90 grados a la derecha

    end_fill()       

def triangle(start, end):
    """Draw triangle from start to end."""
    pass  # TODO
    up()
    goto(start.x, start.y)  
    down()                 #De la linea 31 a 33 hace que la tortuga vaya a la posición que le indiquemos
    begin_fill()           #Inicia el dibujo

    for count in range(3): #Va a realizar el proceso 3 veces
        forward(end.x - start.x) #Avanza la distancia de valor x
        left(120)          #Gira a la izquierda 120 grados (Un triangulo equilatero todos sus angulos son de 60
                           # grados)
    end_fill()

def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
