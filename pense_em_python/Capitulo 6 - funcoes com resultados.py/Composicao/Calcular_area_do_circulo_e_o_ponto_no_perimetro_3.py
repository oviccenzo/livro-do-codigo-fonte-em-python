import math

def distancia3(x18,y18,x19,y19):
    dx1 = x18 - x19
    dy1 = y18 - y19
    dsquard1 = math.sqrt(dx1*dx1 + dy1*dy1)
    result = math.sqrt(dsquard1)
    return (dsquard1)

print(distancia3(1,2,4,8))
