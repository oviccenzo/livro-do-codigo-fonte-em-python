import turtle

bob = turtle.Turtle()
print(bob)

def polyline(t, n, length, angle):
    """Desenha n segmentos de reta com o comprimento dado e
    ângulo (em graus) entre eles. t é um turtle.
    """
    for i in range(n):
        t.fd(length)
        t.left(angle)

polyline(bob, 10,100,90)

turtle.mainloop()