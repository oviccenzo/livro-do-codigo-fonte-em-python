import math

def distancia1(x16,y16,x17,y17):
  dx = x16 - x17
  dy = y16 - y17
  dsquard = pow(dx,2) + pow(dy,2)
  print(f"O resultado do dsquard eh: {dsquard}")
  return dsquard


distancia1(1,2,5,5)

def area3 (radius7):

    return math.pi * radius7 ** 2

def circle_area1(xc1,xy1,xp1,yp1):
  radius7 = distancia1(xc1,xy1,xp1,yp1)

  result = area3(radius7)
  return result

print(f"O resultado do circulo da area eh: {circle_area1(1,2,4,6)}")

