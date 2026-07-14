import math

def distancia3(x18,y18,x19,y19):
  dx1 = x18 - x19
  dy2 = y18 - y19
  dsquard1 = math.pow(dx1,2) + math.pow(dy2,2)
  result = math.sqrt(dsquard1)
  return result

print(f"O resultado do dsquard1 eh: {distancia3(1,2,4,6)}")
