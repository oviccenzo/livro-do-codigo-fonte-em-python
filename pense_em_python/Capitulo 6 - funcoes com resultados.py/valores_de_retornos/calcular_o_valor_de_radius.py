import math

def area(radius4):
    a = math.pi * radius4**2
    return a

radius4 = float(input("Digite o valor do radius: "))
print(f"O valor do resultado eh: {area(radius4)}")