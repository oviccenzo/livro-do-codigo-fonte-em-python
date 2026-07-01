import math

def distancia1(x14,y14,x15,y15):
  dx = x14 - x15
  dy = y14 - y15
  print(f"dx is {dx}")
  print(f"dy is {dy}")
  return 0.0

distancia1(1,2,4,6)

def area3 (radius7):
  return math.pi * radius7 ** 2

def circle_area1(xc1,xy1,xp1,yp1):
  radius7 = distancia1(xc1,xy1,xp1,yp1)

  result = area3(radius7)
  return result

print(f"O resultado do circulo da area eh: {circle_area1(1,2,4,6)}")
