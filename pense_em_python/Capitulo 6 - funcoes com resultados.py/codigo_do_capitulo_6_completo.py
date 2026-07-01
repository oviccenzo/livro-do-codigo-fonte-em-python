# Capitulo 6 Funções com resultado

##Valores de retorno

import math

radians3 = float(input("Digite qualquer número: "))
radius = float(input("Digite qualquer número: "))
expoente = float(input("Digite qualquer número: "))


e = math.exp(expoente)
height = radius * math.sin(radians3)

print(f"O valor dor resultado do expoente de e eh: {e}")
print(f"O valor do resultado radius eh: {height}")

import math

def area(radius4):
  a = math.pi * radius4**2
  return a

radius4 = float(input("Digite qualquer número de radius: "))
print(f"O valor do resultado eh: {area(radius4)}")

import math

def area1(radius5):
  return math.pi * radius5 ** 2

radius5 = float(input("Digite qualquer número de radius: "))
print(f"O valor do resultado eh: {area1(radius5)}")

##Variavies temporais e o valor absoluto

def absolute_value(x6):
  if x6 < 0:
    return -x6
  else:
    return x6

x6 = float(input("Digite qualquer número: "))
print(f"O valor absolute eh: {absolute_value(x6)}")

def absolute_value1(x7):
  if x7 < 0:
    return -x7
  if x7 > 0:
    return x7
absolute_value1(0)

print(absolute_value1(0))

##Desenvolvimento incremental

#####calcular dois ponto dados pelas coordenada

def distancia(x12, y12, x13, y13):
  return 0.0

distancia(1, 2, 4, 6)

def distancia1(x14,y14,x15,y15):
  dx = x14 - x15
  dy = y14 - y15
  print(f"dx is {dx}")
  print(f"dy is {dy}")
  return 0.0

distancia1(1,2,4,6)

import math

def distancia2(x16,y16,x17,y17):
  dx = x16 - y17
  dy = y16 - y17
  dsquared = dx**2 + dy**2
  print(f"dsquared is: {dsquared}")
  return
distancia2(1,2,4,5)

import math

def distancia3(x18,y18,x19,y19):
  dx1 = x18 - y19
  dy1 = y18 - y19
  dsquared1 = dx1 ** 2 + dy1 ** 2
  result = math.sqrt(dsquared1)
  return result

distancia3(1,2,4,6)

##Composição

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

import math
def area3 (radius7):
  return math.pi * radius7 ** 2

def circle_area1(xc1,xy1,xp1,yp1):
  radius7 = distancia1(xc1,xy1,xp1,yp1)


##Funções booleanos

####Retornando a funções booleanos

def is_divisible(x19, y19):
  if x19 % y19 == 0:
    return True
  else:
    return False

print(is_divisible(6,4))
print(is_divisible(6,3))

def is_divisible1(x20, y20):
  return x20 % y20 == 0
print(is_divisible1(6,4))
print(is_divisible1(6,3))

###Funções booleanos incondicionais

def is_divisible2(x21,y21):
  print("x is divisible by y")
  return x21 % y21 == 0

print(is_divisible2(6,4))
print(is_divisible2(6,3))

def is_divisible3(x22,y22):
  if x22 % y22 == True:
    print("x is divisible by y")

def is_between(x,y,z):
  return x <= y <= z

print(is_between(8,9,11))

##Mais recursividade

def factorial(n11):
  if n11 == 0:
    return 1
  else:
    recurse = factorial(n11-1)
    result3 = n11 * recurse
    return result3

print(factorial(3))
print(factorial(4))
print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))

####verificações de tipos

def factorial1(n12):
  if n12 == 0:
    return 1
  else:
    recurse1 = factorial1(n12-1)
    result4 = n12 * recurse1
    return result4

(factorial1(12))

def factorial2(n13):
  if not isinstance(n13, int):
    print("Factorial is only defined for positive integers")
    return None
  elif n13 < 0:
    print("Factorial is not defined for negative integers")
    return None
  elif n13 == 0:
    return 1
  else:
    return n13 * factorial2(n13-1)
print(factorial2("Fred"))
print("\n")
print(factorial2(-2))

