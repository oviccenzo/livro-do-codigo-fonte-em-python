import turtle
import math

bob = turtle.Turtle()
print(bob)

def polyline(t ,n , length ,angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polyline(bob,30,18,12)

turtle.mainloop()
