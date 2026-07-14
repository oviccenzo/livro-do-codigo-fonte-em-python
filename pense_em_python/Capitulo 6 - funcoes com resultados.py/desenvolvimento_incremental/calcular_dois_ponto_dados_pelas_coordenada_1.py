import math

def distancia2(x16,y16,x17,y17):
  dx = x16 - x17
  dy = y16 - y17
  dsquard = dx ** 2 + dy ** 2
  print(f"O resultado dsquard eh: {dsquard}")
  return math.sqrt(dsquard)

print(f"O resultado final do dsquard com sqrt eh:"
      f"{distancia2(1,2,4,5)}")