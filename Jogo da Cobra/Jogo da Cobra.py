import turtle
import time
import random

delay = 0.06

# Ecrã
wn = turtle.Screen()
wn.title("Jogo da Cobra by Heleno")
wn.bgcolor("#ABD651")
wn.setup(width=600, height=600)
wn.tracer(0)

# Cabeça da Cobra
cabeça = turtle.Turtle()
cabeça.speed(0)
cabeça.shape("square")
cabeça.color("#4C7AF4")
cabeça.penup()
cabeça.goto(0, 0)
cabeça.direction = "stop"

# Comida da Cobra
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("#E5481D")
comida.penup()
comida.goto(0, 100)

# Corpo da Cobra
segmentos = []

# Pontuação
pontuação = 0
pontuação_máxima = 0

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PONTUAÇÃO: " + str(pontuação) + "  PONTUAÇÃO MÁXIMA: " + str(pontuação_máxima) , align="center",
          font=("Courier", 24, "bold"))

# Funções
def ir_cima():
    if cabeça.direction != "baixo":
        cabeça.direction = "cima"

def ir_baixo():
    if cabeça.direction != "cima":
        cabeça.direction = "baixo"

def ir_esquerda():
    if cabeça.direction != "direita":
        cabeça.direction = "esquerda"

def ir_direita():
    if cabeça.direction != "esquerda":
        cabeça.direction = "direita"


def move():
    if cabeça.direction == "cima":
        y = cabeça.ycor()
        cabeça.sety(y + 20)

    if cabeça.direction == "baixo":
        y = cabeça.ycor()
        cabeça.sety(y - 20)

    if cabeça.direction == "esquerda":
        x = cabeça.xcor()
        cabeça.setx(x - 20)

    if cabeça.direction == "direita":
        x = cabeça.xcor()
        cabeça.setx(x + 20)

# Ligação com o Teclado
wn.listen()
# WASD
wn.onkeypress(ir_cima, "w")
wn.onkeypress(ir_baixo, "s")
wn.onkeypress(ir_esquerda, "a")
wn.onkeypress(ir_direita, "d" )
# Setas
wn.onkeypress(ir_cima, "Up")
wn.onkeypress(ir_baixo, "Down")
wn.onkeypress(ir_esquerda, "Left")
wn.onkeypress(ir_direita, "Right" )

# Main Game Loop
while True:
    wn.update()

    # Colisão da Cabeça com a Borda
    if cabeça.xcor() > 290 or cabeça.xcor() < -290 or cabeça.ycor() > 290 or cabeça.ycor() < -290:
        time.sleep(1)
        cabeça.goto(0, 0)
        cabeça.direction = "stop"

        #Resetar a Pontuação e Delay
        pontuação = 0
        pen.clear()
        pen.write("PONTUAÇÃO: " + str(pontuação) + "  PONTUAÇÃO MÁXIMA: " + str(pontuação_máxima), align="center",
                  font=("Courier", 24, "bold"))

        delay = 0.06


        # Esconder os segmentos
        for segment in segmentos:
            segment.goto(1000, 1000)

        # Limpar a lista de segmentos
        segmentos.clear()

    # Colisão da Cabeça com a Comida
    if cabeça.distance(comida) < 20:
        # Mover a comida para um lugar aleatório
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        comida.goto(x, y)

        # Adicionar um segmento
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("#4C7AF4")
        novo_segmento.penup()
        segmentos.append(novo_segmento)

        # Adicionar Pontuação
        pontuação += 10

        if pontuação > pontuação_máxima:
            pontuação_máxima = pontuação

        pen.clear()
        pen.write("PONTUAÇÃO: " + str(pontuação) + "  PONTUAÇÃO MÁXIMA: " + str(pontuação_máxima), align="center",
                  font=("Courier", 24, "bold"))

        # Diminuir Delay
        delay *= 0.975

    # Mover os segmentos do fim primeiro
    for index in range(len(segmentos)-1, 0, -1):
        x = segmentos[index-1].xcor()
        y = segmentos[index-1].ycor()
        segmentos[index].goto(x, y)

    # Mover o segmento 0 (primeiro) para onde a cabeça está
    if len(segmentos) > 0:
        x = cabeça.xcor()
        y = cabeça.ycor()
        segmentos[0].goto(x, y)

    move()

    # Colisão da Cabeça com o Corpo
    for segment in segmentos:
        if segment.distance(cabeça) < 20:
            time.sleep(1)
            cabeça.goto(0, 0)
            cabeça.direction = "stop"

            # Esconder os segmentos
            for segment in segmentos:
                segment.goto(1000, 1000)

            # Limpar a lista de segmentos
            segmentos.clear()

            # Resetar a Pontuação e Delay
            pontuação = 0
            pen.clear()
            pen.write("PONTUAÇÃO: " + str(pontuação) + "  PONTUAÇÃO MÁXIMA: " + str(pontuação_máxima), align="center",
                      font=("Courier", 24, "bold"))

            delay = 0.06

    time.sleep(delay)

