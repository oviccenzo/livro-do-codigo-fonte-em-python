##### a mesma composição do codigo anterior usando a função integrada são aplicada a função
# definidas pelos programadores, então podemos usar qualquer tipo de expressão como argumentos
import math
def  print_twice1(bruce3):
    print(bruce3)
    print(bruce3)

print_twice1(' Spam ' * 4)
print_twice1(math.cos(math.pi))
print_twice1(math.sin(2)/2)

# O resultado desse exemplo eh:
#  Spam  Spam  Spam  Spam
#  Spam  Spam  Spam  Spam
# -1.0
# -1.0
# 0.7071067811865476
# 0.7071067811865476
