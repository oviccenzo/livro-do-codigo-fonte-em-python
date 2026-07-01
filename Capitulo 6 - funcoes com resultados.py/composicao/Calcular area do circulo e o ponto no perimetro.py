import math

def distancia(x12, y12, x13, y13):
  return 0.0

distancia(1, 2, 4, 6)

def area2(radius6):
  radius6 = float(input("Digite qualquer numero: "))
  return math.pi * radius6 ** 2

def circle_area(xc, yc, xp, yp):
  radius6 = distancia(xc, yc, xp, yp)
  result = area2(radius6)
  return result

print(f"O resultado do circulo da area eh: {circle_area(1,2,4,6)}")