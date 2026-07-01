####Calcular area do circulo e o ponto no perimetro

import math

def area2(radius6):
  radius6 = float(input("Digite qualquer numero: "))
  return math.pi * radius6 ** 2

def circle_area(xc, yc, xp, yp):
  radius6 = distancia(xc, yc, xp, yp)
  result = area2(radius6)
  return result

circle_area(1,2,4,6)

