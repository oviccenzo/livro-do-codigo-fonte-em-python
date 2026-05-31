####calcular qualquer valor de graus radiano

import math
degrees2 = float(input("Digite qualquer valor de graus: "))

x = math.sin(degrees2 / 360.0 * 2 * math.pi)
x1 = math.exp(math.log(x + 1))
print(f"O resultado da expressao eh: {x}")
print(f"O resultado da expressao eh: {x1}")

# O resultado desse exemplo eh:
# Digite qualquer valor de graus: 2000
# O resultado da expressao eh: -0.3420201433256638
# O resultado da expressao eh: 0.6579798566743362