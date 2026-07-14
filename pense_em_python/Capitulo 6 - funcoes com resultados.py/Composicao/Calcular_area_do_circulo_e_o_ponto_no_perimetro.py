import  math

def distancia(x14,y14,x15,y15):
  dx = x14 - x15 #1 - 4 = -3
  dy = y14 - y15 #2 - 6 = -4
  print(f"dx is {dx}")
  print(f"dy is {dy}")
  return 0.0


distancia(1,2,4,6)

def area2(radius6):
    radius6 = float(input("Digite o valor do radius: "))
    return math.pi * radius6**2

def circle_area(xc,yc,xp,yp):
    radius6 = distancia(xc,yc,xp,yp)
    resultado = area2(radius6)
    return resultado
print(f"O resultado do circulo da area eh: {circle_area(1,2,4,6)}")