import turtle
import math

bob = turtle.Turtle()
print(bob)

def arc(t ,r, angle):
    arc_angle = 2 * math.pi * r * angle / 360
    n = int(arc_angle / 3) + 1
    step_length = arc_angle / n
    step_angle = angle / n
    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

arc(bob,100,90)
turtle.mainloop()
