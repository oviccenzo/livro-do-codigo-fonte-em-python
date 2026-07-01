import math

radians3 = float(input("Digite qualquer número: "))
radius = float(input("Digite qualquer número: "))
expoente = float(input("Digite qualquer número: "))


e = math.exp(expoente)
height = radius * math.sin(radians3)

print(f"O valor dor resultado do expoente de e eh: {e}")
print(f"O valor do resultado radius eh: {height}")