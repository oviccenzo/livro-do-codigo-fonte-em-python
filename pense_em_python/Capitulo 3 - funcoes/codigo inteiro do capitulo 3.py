# Capitulo 3: funcoes

###3.1 - chamada de função usando o type , int, str, o type eh para identificar o numero e palavra e o int usado para mostrar o valor sem o ponto flutuante e o float mostrar varios ponto flutuante

print(type(42))

print(int('32'))

# int('helo')
# ValueError: invalid literal for int() with base 10: 'helo'

print(int(3.99999))

print(int(-2.3))

print(float(32))

(float('3.14159'))

(str('32'))

(str(3.14159))

###3.2 funcoes matematica e codificando o programa que calcular o radiasno

####importação da biblioteca math

import math
math

####primeiro exemplo usa math.log10 para calcular a proporção de sinal ruído decibeis

import math
signal_power = int(input("Digite a potencial de sinal: "))
noise_power = int(input("Digite a potencial de ruido: "))
decibels = int(input("Digite a pontecial de decibeis: "))

ratio = signal_power / noise_power
decibels = 10 * math.log10(ratio)
radians = 0.7
height = math.sin(radians)
print(f"O resultado do decibéis eh: {decibels}")
print(f"O resultado da altura eh: {height}")

####segundo exemplo encontra o seno de radians.O nome da variável indica sin e outras funções.

import math
degrees = 45
radians1 = degrees / 360.0 * 2 * math.pi
math.sin(radians1)
print(f"O resultado do seno eh: {math.sin(radians1)}")

###composição

####calcular raiz ao quadrado


import math

print(f"O valor da raiz ao quadrado eh: {math.sqrt(2)/2.0}")
print(f"O valor da raiz ao quadrado eh: {math.sqrt(3)/2.0}")
print(f"O valor da raiz ao quadrado eh: {math.sqrt(4)/2.0}")
print(f"O valor da raiz ao quadrado eh: {math.sqrt(5)/2.0}")
print(f"O valor da raiz ao quadrado eh: {math.sqrt(6)/2.0}")
print(f"O valor da raiz ao quadrado eh: {math.sqrt(7)/2.0}")
print(f"O valor da raiz ao quadrado eh: {math.sqrt(8)/2.0}")
print(f"O valor da raiz ao quadrado eh: {math.sqrt(9)/2.0}")

####calcular qualquer valor de graus radiano

import math
degrees2 = float(input("Digite qualquer valor de graus: "))

x = math.sin(degrees2 / 360.0 * 2 * math.pi)
x1 = math.exp(math.log(x + 1))
print(f"O resultado da expressao eh: {x}")
print(f"O resultado da expressao eh: {x1}")

####Calcular qualquer valor de hora por 60 minutos

hours = float(input("Digite qualquer valor de horas: "))

minute = hours * 60
print(f"O resultado da expressao eh: {minute}")

####exemplo da função def o print_lyric

def print_lyric():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

print_lyric()

def print_lyric1():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

print(print_lyric1)

def print_lyric2():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

print(type(print_lyric2))

####a função nova e a mesma que a das funções integrada

def print_lyric3():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

(print_lyric3())

####a função se chama repeat_lyric

def print_lyric4():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

def repeat_lyric5():
  print_lyric()

print_lyric4()
print('\n')
repeat_lyric5()

####juntando as funções do codigo anterior que seria print_lyric e repeat_lyric

def print_lyric6():
  print("I'm a lumberjack, and I'm okay.")
  print("I sleep all night and I work all day.")

def repeat_lyric7():
  print_lyric6()
  print_lyric6()

repeat_lyric7()

####parâmetros e argumentos
# Dentro da função os argumentos são atribuídos a variaveis chamada parâmetros

import math
def print_twice(bruce,bruce1):
  print(bruce * 2)
  print(bruce1 * 3)

print_twice(' spam ', ' spam ') #6 palavras spam
print_twice(42 , 44)
print_twice(math.pi,math.pi)
print_twice(' spam '* 3,' spam ' * 4) # 12 palavras spam
print_twice(math.sin(math.pi), math.sin(math.pi))

####a mesma composição do codigo anterior usando a função integrada são aplicada a função definidas
# pelos programadores, então podemos usar qualquer tipo de expressão como argumentos

import math
def print_twice1(bruce3):
  print(bruce3)
  print(bruce3)

print_twice1(' Spam ' * 4)
print_twice1(math.cos(math.pi))
print_twice1(math.sqrt(2)/2)

def print_twice2(bruce4):
  print(bruce4)
  print(bruce4)

michael = 'Eric , the half a bee'
print_twice2(michael)

####As variáveis e os parâmetros são locais

def print_twice2(bruce5):
    print(bruce5)
    print(bruce5)

michael = "Eric, the half a bee"
print_twice2(michael)

###funcoes com resultados e funcoes nula

####a chamada da função matematica

import math

radians2 = float(input("Digite qualquer valor de radians: "))
num3 = float(input("Digite qualquer valor: "))

x = math.cos(radians2)
golden = (math.sqrt(num3) + 1) / 2
print(f"O resultado da expressao eh: {x}")
print(f"O resultado da expressao eh: {golden}")

####chamada da função modo interativo no python que exiba o resultado desse função

import math

print(math.sqrt(5))
print(math.sqrt(6))
print(math.sqrt(7))
print(math.sqrt(8))
print(math.sqrt(9))
print(math.sqrt(10))

####O valor none não é a mesma que a string 'None'

def print_twice3(bruce6):
  print(bruce6)
  print(bruce6)

result = print_twice3('Bing')

print(type(result))

####O resultado do capitulo:
# <class 'int'>
# 32
# 3
# -2
# 32.0
# Digite a potencial de sinal: 8
# Digite a potencial de ruido: 88
# Digite a pontecial de decibeis: 87
# O resultado do decibéis eh: -10.41392685158225
# O resultado da altura eh: 0.644217687237691
# O resultado do seno eh: 0.7071067811865475
# O valor da raiz ao quadrado eh: 0.7071067811865476
# O valor da raiz ao quadrado eh: 0.8660254037844386
# O valor da raiz ao quadrado eh: 1.0
# O valor da raiz ao quadrado eh: 1.118033988749895
# O valor da raiz ao quadrado eh: 1.224744871391589
# O valor da raiz ao quadrado eh: 1.3228756555322954
# O valor da raiz ao quadrado eh: 1.4142135623730951
# O valor da raiz ao quadrado eh: 1.5
# Digite qualquer valor de graus: 123
# O resultado da expressao eh: 0.838670567945424
# O resultado da expressao eh: 1.838670567945424
# Digite qualquer valor de horas: 342
# O resultado da expressao eh: 20520.0
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# <function print_lyric1 at 0x7fa1d76d40d0>
# <class 'function'>
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
#
#
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
# I'm a lumberjack, and I'm okay.
# I sleep all night and I work all day.
#  spam  spam
#  spam  spam  spam
# 84
# 132
# 6.283185307179586
# 9.42477796076938
#  spam  spam  spam  spam  spam  spam
#  spam  spam  spam  spam  spam  spam  spam  spam  spam  spam  spam  spam
# 2.4492935982947064e-16
# 3.6739403974420594e-16
#  Spam  Spam  Spam  Spam
#  Spam  Spam  Spam  Spam
# -1.0
# -1.0
# 0.7071067811865476
# 0.7071067811865476
# Eric , the half a bee
# Eric , the half a bee
# Eric, the half a bee
# Eric, the half a bee
# Digite qualquer valor de radians: 234
# Digite qualquer valor: 23
# O resultado da expressao eh: 0.048633500538969116
# O resultado da expressao eh: 2.8979157616563596
# 2.23606797749979
# 2.449489742783178
# 2.6457513110645907
# 2.8284271247461903
# 3.0
# 3.1622776601683795
# Bing
# Bing
# <class 'NoneType'>

##Exercicio do capitulo 3

####Exercicio 3.1
# Escreva uma função chamada right_justify, que receba uma string chamada s
# como parâmetro e exiba a string com espaços suficientes à frente para que a
# última letra da string esteja na coluna 70 da tela:
# >>> right_justify(‘monty’)
# monty
# Dica: Use concatenação de strings e repetição. Além disso, o Python oferece
# uma função integrada chamada len, que apresenta o comprimento de uma
# string, então o valor de len(‘monty’) é 5.

##Exercicio 3.2
# Um objeto de função é um valor que pode ser atribuído a uma variável ou
# passado como argumento. Por exemplo, do_twice é uma função que toma umobjeto de função
# como argumento e o chama duas vezes:
# def do_twice(f):
# f()
# f()
# Aqui está um exemplo que usa do_twice para chamar uma função chamada
# print_spam duas vezes:
# def print_spam():
# print(‘spam’)
# do_twice(print_spam)
# 1. Digite este exemplo em um script e teste-o.
# 2. Altere do_twice para que receba dois argumentos, um objeto de
# função e um valor, e chame a função duas vezes, passando o valor como um
# argumento.
# 3. Copie a definição de print_twice que aparece anteriormente neste
# capítulo no seu script.
# 4. Use a versão alterada de do_twice para chamar print_twice duas vezes,
# passando ‘spam’ como um argumento.
# 5. Defina uma função nova chamada do_four que receba um objeto de
# função e um valor e chame a função quatro vezes, passando o valor como um
# parâmetro. Deve haver só duas afirmações no corpo desta função, não quatro.
# Solução: http://thinkpython2.com/code/do_four.py.


###Exercicio 3.3

# Nota: Este exercício deve ser feito usando-se apenas as instruções e os outros
# recursos que aprendemos até agora.1. Escreva uma função que desenhe uma grade como a seguinte:

#+ - - - - + - - - - +
#| | |
#| | |
#| | |
#| | |
#+ - - - - + - - - - +
#| | |
#| | |
#| | |
#| | |
#+ - - - - + - - - - +


# Dica: para exibir mais de um valor em uma linha, podemos usar uma
# sequência de valores separados por vírgula:
# print(‘+’, ‘-’)
# Por padrão, print avança para a linha seguinte, mas podemos ignorar
# esse comportamento e inserir um espaço no fim, desta forma:
# print(‘+’, end=’ ’)
# print(‘-’)
# A saída dessas instruções é ‘+ -’.
# Uma instrução print sem argumento termina a linha atual e vai para apróxima linha.
# 2. Escreva uma função que desenhe uma grade semelhante com quatro
# linhas e quatro colunas.
# Solução: http://thinkpython2.com/code/grid.py. Crédito: Este exercício é
# baseado em outro apresentado por Oualline, em Practical C Programming,
# Third Edition, O’Reilly Media, 1997.
