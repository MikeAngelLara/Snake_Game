import turtle
import time
import random

delay = 0.01
segmentos_cuerpo = []
puntuacion = 0
mayor_puntuacion = 0

ventana = turtle.Screen()

#titulo
ventana.title("La Culebrita")

#tamaño de la ventana
ventana.setup(width=600, height=600)

#color de fondo
ventana.bgcolor("light green")

#configuracion de la cabeza
#Turtle obj 
head = turtle.Turtle()
#para que se quede fijo
head.speed(0)
#forma
head.shape('square')
#Color de la cabeza
head.color("green")
#Para no dejar rastro de la animacion
head.penup()
#center
head.goto(0,0)
#Espere que le de otra direccion
head.direction = "stop"


#Configuracion de la comida 
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)
comida.direction = "stop"


#puntuacion
text = turtle.Turtle()
text.speed(0)
text.color('gray')
text.penup()
text.hideturtle()
text.goto(0,260)
text.write(f'Puntuación: 0     Mayor Puntuación: 0', align="center", font=("Arial", 24))


#Funciones
def mov():
    if head.direction == "up":
        #almacenar el valor actual de la coord Y
        y = head.ycor()
        head.sety(y + 10)

    if head.direction == "down":
        #almacenar el valor actual de la coord Y
        y = head.ycor()
        head.sety(y - 10)

    if head.direction == "right":
        #almacenar el valor actual de la coord Y
        y = head.xcor()
        head.setx(y + 10)

        
    if head.direction == "left":
        #almacenar el valor actual de la coord Y
        y = head.xcor()
        head.setx(y - 10)


#direccion hacia arriba
def dir_up():
    head.direction = "up"
#Para conectar teclado
ventana.listen()
ventana.onkeypress(dir_up, "Up")


#direccion hacia abajo
def dir_down():
    head.direction = "down"
#Para conectar teclado
ventana.listen()
ventana.onkeypress(dir_down, "Down")


#direccion hacia la derecha
def dir_right():
    head.direction = "right"
#Para conectar teclado
ventana.listen()
ventana.onkeypress(dir_right, "Right")


#direccion hacia la izquierda
def dir_left():
    head.direction = "left"
#Para conectar teclado
ventana.listen()
ventana.onkeypress(dir_left, "Left")




while True:
    ventana.update()

    #choques con los bordes
    if head.xcor() > 280 or head.xcor() < -280 or head.ycor() > 280 or head.ycor() < -280:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        #esconder segmentos 
        for segment in segmentos_cuerpo:
            segment.goto(1000, 1000)

        segmentos_cuerpo.clear()
        puntuacion = 0
        text.clear()
        text.write(f'Puntuación: {puntuacion}     Mayor Puntuación: {mayor_puntuacion}', align="center", font=("Arial", 24))


    #choque de la cabeza vs comida
    if head.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color("blue")
        new_segment.penup()
        segmentos_cuerpo.append(new_segment)
        print("nuevo segmento")


        #Actualizar puntuacion
        puntuacion += 10
        if puntuacion > mayor_puntuacion:
            mayor_puntuacion = puntuacion
        text.clear()
        text.write(f'Puntuación: {puntuacion}     Mayor Puntuación: {mayor_puntuacion}', align="center", font=("Arial", 24))

    
    total_seg = len(segmentos_cuerpo)

    for i in range(total_seg -1, 0, -1):
        x = segmentos_cuerpo[i-1].xcor()
        y = segmentos_cuerpo[i-1].ycor()
        segmentos_cuerpo[i].goto(x,y)

    if total_seg > 0:
        x = head.xcor()
        y = head.ycor()
        segmentos_cuerpo[0].goto(x, y)

    mov()


    #Choques con el cuerpo
    for segment in segmentos_cuerpo:
        if segment.distance(head) < 10:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"

            for segment in segmentos_cuerpo:
                segment.goto(1000, 1000)

            segmentos_cuerpo.clear()
            puntuacion = 0
            text.clear()
            text.write(f'Puntuación: {puntuacion}     Mayor Puntuación: {mayor_puntuacion}', align="center", font=("Arial", 24))


    time.sleep(delay)

turtle.done()