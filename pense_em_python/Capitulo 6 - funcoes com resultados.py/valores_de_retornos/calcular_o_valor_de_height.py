import math

radians3 = float(input("Digite o valor do radians: "))
radius = float(input("Digite o valor do radios: "))
expoente = float(input("Digite o valor do expoente: "))

e = math.exp(expoente)
height = radius * math.sin(radians3)

print(f"O valor dos resultados do expoente de e eh: {e}")
print(f"O valor do resultado radius eh: {height}")