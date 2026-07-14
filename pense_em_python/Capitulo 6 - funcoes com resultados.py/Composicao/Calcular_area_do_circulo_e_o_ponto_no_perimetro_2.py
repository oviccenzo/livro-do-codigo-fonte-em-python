import math

def distancia2(x16,y16,x17,y17):
  dx = x16 - x17
  dy = y16 - y17
  dsquard = math.pow(dx,2) + math.pow(dy,2)
  print(f"O resultado do dsquard eh: {dsquard}")
  return math.sqrt(dsquard) # Return the actual radius

print(f"O resultado final do dsquard com sqrt eh: {distancia2(1,2,4,5)}")

