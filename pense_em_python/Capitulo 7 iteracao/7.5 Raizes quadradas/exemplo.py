a = 4
x = 3
epsilon = 0.0000001
y = ((x + a /x)/2)
print(y)

x = y
y = ((x + a / x) / 2)
print(y)

x = y
y = ((x + a / x) / 2)
print(y)

x = y
y = ((x + a / x) / 2)
print(y)

while True:
    print(x)
    y = (x + a /x) /2

    if abs(y - x) < epsilon:
        break

    x = y

print("Raiz quadrada aproximado de y eh: ",y)
print("Raiz quadrada aproximado de x eh: ",x)