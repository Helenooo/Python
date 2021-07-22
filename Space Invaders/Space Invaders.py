import turtle
import os
import math
import random

# Ecrã
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders by Heleno")
wn.setup(width=603, height=603)
wn.bgpic("esp.gif")
wn.tracer(0)

# Registo das Formas
wn.register_shape("nave.gif")
wn.register_shape("inimigo.gif")
wn.register_shape("bala.gif")

# Borda
pen_borda = turtle.Turtle()
pen_borda.speed(0)
pen_borda.color("white")
pen_borda.penup()
pen_borda.goto(-300, -300)
pen_borda.pendown()
pen_borda.pensize(3)
pen_borda.hideturtle()
for side in range (4):
    pen_borda.fd(600)
    pen_borda.lt(90)

# Pontuação
pontuação = 0
pen_pontuação = turtle.Turtle()
pen_pontuação.speed(0)
pen_pontuação.color("white")
pen_pontuação.shape("square")
pen_pontuação.penup()
pen_pontuação.hideturtle()
pen_pontuação.goto(-291, 274)
pen_pontuação.write("PONTUAÇÃO: " + str(pontuação), align="left", font=("Courier", 19, "bold"))

# Jogador
jogador = turtle.Turtle()
jogador.speed(0)
jogador.color("cyan")
jogador.shape("nave.gif")
jogador.penup()
jogador.goto(0, -250)
jogador.setheading(90)
velocidade_jogador = 15
estado_jogador = "vivo"

# Número de Inimigos
número_de_inimigos = 7
# Lista vazia de Inimigos
inimigos = []
# Adicionar inimigos à lista
for i in range(número_de_inimigos):
    # Inimigo
    inimigos.append(turtle.Turtle())

for inimigo in inimigos:
    inimigo.speed(0)
    inimigo.color("lightgreen")
    inimigo.shape("inimigo.gif")
    inimigo.penup()
    x = random.randint(-200, 200)
    y = random.randint(100, 250)
    inimigo.goto(x, y)
    velocidade_inimigo = 1.5

# Bala do Jogador
bala = turtle.Turtle()
bala.speed(0)
bala.color("yellow")
bala.shape("bala.gif")
bala.setheading(90)
bala.penup()
bala.shapesize(0.5, 0.5)
bala.hideturtle()
velocidade_bala = 17
estado_bala = "a_postos"

# Game Over
GO = turtle.Turtle()
GO.speed(0)
GO.shape("square")
GO.color("red")
GO.penup()
GO.goto(0, 30)
GO.hideturtle()

# Mensagem para o Jogador
jogar_novamente = turtle.Turtle()
jogar_novamente.speed(0)
jogar_novamente.shape("square")
jogar_novamente.color("white")
jogar_novamente.penup()
jogar_novamente.goto(0, -10)
jogar_novamente.hideturtle()

# Funções
def mover_direita():
    if estado_jogador == "vivo":
        x = jogador.xcor()
        if x > 270:
            x = 270
        jogador.setx(x + velocidade_jogador)


def mover_esquerda():
    if estado_jogador == "vivo":
        x = jogador.xcor()
        if x < -270:
            x = -270
        jogador.setx(x - velocidade_jogador)

def disparo():
    if estado_jogador == "vivo":
        global estado_bala
        if estado_bala == "a_postos":
            os.system("afplay laser.wav&")
            estado_bala = "disparo"
            x = jogador.xcor()
            bala.showturtle()
            bala.goto(x, -240)

def reset():
    global estado_jogador
    if estado_jogador == "morto":
        # Jogador
        jogador.showturtle()
        jogador.goto(0, -250)
        # Inimigos
        global velocidade_inimigo
        velocidade_inimigo = 1.5
        for inimigo in inimigos:
            inimigo.showturtle()
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            inimigo.goto(x, y)
        # Bala
        global estado_bala
        estado_bala = "a_postos"
        bala.showturtle()
        # Tirar Mensagens do Ecrã
        GO.clear()
        jogar_novamente.clear()
        # Estado do Jogador
        estado_jogador = "vivo"

# Ligação ao Teclado
wn.listen()
wn.onkeypress(mover_esquerda, "a")
wn.onkeypress(mover_direita, "d")
wn.onkeypress(mover_esquerda, "Left")
wn.onkeypress(mover_direita, "Right")
wn.onkeypress(disparo, "space")
wn.onkeypress(reset, "r")

# Loop Principal do Jogo
while True:
    wn.update()

    for inimigo in inimigos:
        # Movimento dos Inimigos
        x = inimigo.xcor()
        inimigo.setx(x + velocidade_inimigo)

    # Movimento da Bala
    if estado_bala == "disparo":
        y = bala.ycor()
        bala.sety(y + velocidade_bala)

    # Colisão da Bala com a Borda
    if bala.ycor() > 295:
        bala.hideturtle()
        estado_bala = "a_postos"

    for inimigo in inimigos:
        # Colisão da Bala com os Inimigos
        if bala.distance(inimigo) < 20:
            os.system("afplay explosão.wav&")
            estado_bala = "a_postos"
            bala.hideturtle()
            bala.goto(0, -400)
            x = random.randint(-200, 200)
            y = random.randint(100, 250)
            inimigo.goto(x, y)
            pontuação += 10
            pen_pontuação.clear()
            pen_pontuação.write("PONTUAÇÃO: " + str(pontuação), align="left", font=("Courier", 19, "bold"))

    # Colisão do Jogador com o Inimigo:
    for inimigo in inimigos:
        if inimigo.ycor() < -235:
            jogador.hideturtle()
            inimigo.hideturtle()
            bala.hideturtle()
            bala.goto(1000, 1000)
            estado_bala = "disparo"
            velocidade_inimigo = 0
            # Pontuação
            pontuação = 0
            pen_pontuação.clear()
            pen_pontuação.write("PONTUAÇÃO: " + str(pontuação), align="left", font=("Courier", 19, "bold"))
            # Game Over
            GO.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
            # Mensagem para o Jogador
            jogar_novamente.write("Para jogar outra vez pressiona R", align="center", font=("Courier", 20, "bold"))
            # Estado do Jogador
            estado_jogador = "morto"

    for inimigo in inimigos:
        # Movimento do Inimigo para Trás e para Baixo
        if inimigo.xcor() > 270 or inimigo.xcor() < -270:
            for inimigo in inimigos:
                y = inimigo.ycor()
                inimigo.sety(y - 40)
                velocidade_inimigo *= -1