import turtle

bob = turtle.Turtle()
print(bob)

def polygon(t,length):
    for i in range(4):
        t.fd(length)
        t.left(90)

polygon(bob,100)

turtle.mainloop()