import turtle
import math

bob = turtle.Turtle()
print(bob)

def arc(t,r,angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def polygon(t, n, length, angle):
    angle = 36.0 / n
    polyline(t, n, length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polygon(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)




polyline(bob,200,3,3)

polygon(bob,23,45,34)

circle(bob, 100)

turtle.mainloop()
