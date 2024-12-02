import turtle

def desenhar_coracao():
    janela = turtle.Screen()
    janela.bgcolor("white")

    # Configura o turtle
    amor = turtle.Turtle()
    amor.color("red")
    amor.pensize(2)
    amor.speed(2)

    # Desenha um coração
    amor.begin_fill()
    amor.left(140)
    amor.forward(180)
    amor.circle(-90, 200)
    amor.left(120)
    amor.circle(-90, 200)
    amor.forward(180)
    amor.end_fill()

    # Escreve uma mensagem dentro do coração
    amor.penup()
    amor.goto(-50, -20)
    amor.color("white")
    amor.pendown()
    amor.write("Você é especial!", font=("Arial", 16, "bold"))

    # Finaliza
    amor.hideturtle()
    janela.mainloop()

print(desenhar_coracao())
