import math

def area(radius5):
    a = math.pi * radius5 ** 2
    return a

radius5 = float(input("Digite o valor do radius: "))
print(f"O valor do resultado eh: {area(radius5)}")