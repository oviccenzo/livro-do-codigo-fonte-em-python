import turtle

def square(t):
    for i in range(6):
        t.fd((100))
        t.lt(90)

bob = turtle.Turtle()

square(bob)

turtle.mainloop()

