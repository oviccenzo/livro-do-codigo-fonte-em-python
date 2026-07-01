import math

def distancia3(x18,y18,x19,y19):
  dx1 = x18 - y19
  dy1 = y18 - y19
  dsquared1 = dx1 ** 2 + dy1 ** 2
  result = math.sqrt(dsquared1)
  return result

distancia3(1,2,4,6)