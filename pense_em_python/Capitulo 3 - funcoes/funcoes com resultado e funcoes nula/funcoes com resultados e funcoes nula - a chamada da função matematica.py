####A chamada da função matemática
import math

radians2 = float(input("Digite qualquer valor de radians: "))
num3 = float(input("Digite qualquer valor: "))

x = math.cos(radians2)
golden = (math.sqrt(num3) + 1) / 2
print(f"O resultado da expressao de x eh: {x}")
print(f"O resultado da expressao de golden eh: {golden}")

# O resultado desse exemplo eh:
# Digite qualquer valor de radians: 1202
# Digite qualquer valor: 923
# O resultado da expressao de x eh: -0.334250615730526