import math
def area(radius4):
    a = math.pi * math.pow(radius4,2)
    return a

radius4 = float(input("Digite qualquer número de radius: "))
print(f"O valor do resultado eh: {area(radius4)}")