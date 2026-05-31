###3.1 - chamada de função usando o type , int, str, o type eh para identificar o numero e palavra e o int usado para mostrar o valor sem o ponto flutuante e o float mostrar varios ponto flutuante

print(type(42))

print(int('32'))

# print(int('helo'))
# ValueError: invalid literal for int() with base 10: 'helo'

print(int(3.99999))
print(int(-2.3))
print(float(32))
print(float('3.14159'))
print(str('32'))
print(str(3.14159))

# O resultado desse exemplo eh:
# <class 'int'>
# 32
# 3
# -2
# 32.0
# 3.14159
# 32
# 3.14159
