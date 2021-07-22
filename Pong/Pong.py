import turtle

wn = turtle.Screen()
wn.title("Pong by Heleno")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Pontuação
pontuação_A = 0
pontuação_B = 0

# Barra A
barra_A = turtle.Turtle()
barra_A.speed(0)
barra_A.shape("square")
barra_A.color("white")
barra_A.shapesize(stretch_wid=5, stretch_len=1)
barra_A.penup()
barra_A.goto(-350, 0)

# Barra B
barra_B = turtle.Turtle()
barra_B.speed(0)
barra_B.shape("square")
barra_B.color("white")
barra_B.shapesize(stretch_wid=5, stretch_len=1)
barra_B.penup()
barra_B.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("square")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dX = 0.55
bola.dY = 0.55

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("JOGADOR A: " + str(pontuação_A) + "  JOGADOR B: " + str(pontuação_B), align="center", font=("Courier", 24, "bold"))

# Pen GO
GO = turtle.Turtle()
GO.speed(0)
GO.color("red")
GO.penup()
GO.hideturtle()
GO.goto(0, 0)

# Vencedor A
vencedor_A = turtle.Turtle()
vencedor_A.speed(0)
vencedor_A.color("cyan")
vencedor_A.penup()
vencedor_A.hideturtle()
vencedor_A.goto(0, -30)

# Vencedor B
vencedor_B = turtle.Turtle()
vencedor_B.speed(0)
vencedor_B.color("cyan")
vencedor_B.penup()
vencedor_B.hideturtle()
vencedor_B.goto(0, -30)

# Reset
reset = turtle.Turtle()
reset.speed(0)
reset.color("white")
reset.penup()
reset.hideturtle()
reset.goto(0, -55)


# Função
def barra_A_cima():
    y = barra_A.ycor()
    y += 20
    barra_A.sety(y)

def barra_A_baixo():
    y = barra_A.ycor()
    y -= 20
    barra_A.sety(y)

def barra_B_cima():
    y = barra_B.ycor()
    y += 20
    barra_B.sety(y)

def barra_B_baixo():
    y = barra_B.ycor()
    y -= 20
    barra_B.sety(y)

def resetGame():
    # Pontuação
    pontuação_A = 0
    pontuação_B = 0

    # Barra A
    barra_A.goto(-350, 0)

    # Barra B
    barra_B.goto(350, 0)

    # Bola
    bola = turtle.Turtle()
    bola.speed(0)
    bola.shape("square")
    bola.color("white")
    bola.penup()
    bola.goto(0, 0)

    #Clear and Write Score
    GO.clear()
    GO.write("")
    vencedor_A.clear()
    vencedor_A.write("")
    vencedor_B.clear()
    vencedor_B.write("")
    pen.clear()
    pen.write("JOGADOR A: " + str(pontuação_A) + "  JOGADOR B: " + str(pontuação_B), align="center",
              font=("Courier", 24, "bold"))
    reset.clear()

    # Movimento da Bola
    bola.dX = 0.55
    bola.dY = 0.55
    bola.setx(bola.xcor() + bola.dX)
    bola.sety(bola.ycor() + bola.dY)

    # Loop Principal do Jogo
    while True:
        wn.update()

        # Movimento da Bola
        bola.setx(bola.xcor() + bola.dX)
        bola.sety(bola.ycor() + bola.dY)

        # Verificação da Borda
        if bola.ycor() > 290:
            bola.sety(290)
            bola.dY *= -1

        if bola.ycor() < -290:
            bola.sety(-290)
            bola.dY *= -1

        if bola.xcor() > 390:
            bola.goto(0, 0)
            bola.dX *= -1
            pontuação_A += 1
            pen.clear()
            pen.write("JOGADOR A: " + str(pontuação_A) + "  JOGADOR B: " + str(pontuação_B), align="center",
                      font=("Courier", 24, "bold"))

        if bola.xcor() < -390:
            bola.goto(0, 0)
            bola.dX *= -1
            pontuação_B += 1
            pen.clear()
            pen.write("JOGADOR A: " + str(pontuação_A) + "  JOGADOR B: " + str(pontuação_B), align="center",
                      font=("Courier", 24, "bold"))

        # Colisão entre Barras e Bola
        if (bola.xcor() > 340 and bola.xcor() < 350) and (
                bola.ycor() < barra_B.ycor() + 40 and bola.ycor() > barra_B.ycor() - 40):
            bola.setx(340)
            bola.dX *= -1

        if (bola.xcor() < -340 and bola.xcor() > -350) and (
                bola.ycor() < barra_A.ycor() + 40 and bola.ycor() > barra_A.ycor() - 40):
            bola.setx(-340)
            bola.dX *= -1
        # Game Over A
        if pontuação_A == 5:
            # Pen GO
            GO.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
            # Pen Vencedor A
            vencedor_A.write("Vence o Jogador A", align="center", font=("Courier", 24, "bold"))
            # Bola
            bola.color("black")
            bola.setx(0)
            bola.sety(0)
            bola.clear()
            # Reset
            reset.write("Pressiona SPACE para jogar de novo", align="center", font=("Courier", 20, "bold"))
        # Game Over B
        if pontuação_B == 5:
            # Pen GO
            GO.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
            # Pen Vencedor B
            vencedor_B.write("Vence o Jogador B", align="center", font=("Courier", 24, "bold"))
            # Bola
            bola.color("black")
            bola.setx(0)
            bola.sety(0)
            bola.clear()
            # Reset
            reset.write("Pressiona SPACE para jogar de novo", align="center", font=("Courier", 20, "bold"))

# Ligação ao Teclado
wn.listen()
wn.onkeypress(barra_A_cima, "w")
wn.onkeypress(barra_A_baixo, "s")
wn.onkeypress(barra_B_cima, "Up")
wn.onkeypress(barra_B_baixo, "Down")
wn.onkeypress(resetGame, "space")


# Loop Principal do Jogo
while True:
    wn.update()

    # Movimento da Bola
    bola.setx(bola.xcor() + bola.dX)
    bola.sety(bola.ycor() + bola.dY)

    # Verificação da Borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dY *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dY *= -1

    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dX *= -1
        pontuação_A += 1
        pen.clear()
        pen.write("JOGADOR A: " + str(pontuação_A) + "  JOGADOR B: " + str(pontuação_B), align="center",
                  font=("Courier", 24, "bold"))

    if bola.xcor() < -390:
        bola.goto(0, 0)
        bola.dX *= -1
        pontuação_B += 1
        pen.clear()
        pen.write("JOGADOR A: " + str(pontuação_A) + "  JOGADOR B: " + str(pontuação_B), align="center",
                  font=("Courier", 24, "bold"))

    # Colisão entre Barras e Bola
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < barra_B.ycor() + 40 and bola.ycor() > barra_B.ycor() - 40):
        bola.setx(340)
        bola.dX *= -1

    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < barra_A.ycor() + 40 and bola.ycor() > barra_A.ycor() - 40):
        bola.setx(-340)
        bola.dX *= -1

    # Game Over A
    if pontuação_A == 5:
        # Pen GO
        GO.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
        # Pen Vencedor A
        vencedor_A.write("Vence o Jogador A", align="center", font=("Courier", 24, "bold"))
        # Bola
        bola.color("black")
        bola.setx(0)
        bola.sety(0)
        bola.clear()
        # Reset
        reset.write("Pressiona SPACE para jogar de novo", align="center", font=("Courier", 20, "bold"))

    # Game Over B
    if pontuação_B == 5:
        # Pen GO
        GO.write("GAME OVER", align="center", font=("Courier", 50, "bold"))
        # Pen Vencedor B
        vencedor_B.write("Vence o Jogador B", align="center", font=("Courier", 24, "bold"))
        # Bola
        bola.color("black")
        bola.setx(0)
        bola.sety(0)
        bola.clear()
        # Reset
        reset.write("Pressiona SPACE para jogar de novo", align="center", font=("Courier", 20, "bold"))