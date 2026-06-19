# Capitulo 2: variaveis e tipos

###2.1 instrucao e atribuicao

message = 'and now for something completely different'
n = 17
pi = 3.1415926535897932
print(message)
print(n)
print(pi)

# 76trombones = 'big parede'
#    76trombones = 'big parede'
    #  ^
# SyntaxError: invalid decimal literal
trombones = 'big parece'
print(trombones)

# mora@ = 1000000
          # ^
# SyntaxError: invalid syntax
mora = 1000000
print(mora)

# class = 'Advanced Theoretical Zymurgy'
#           ^
# SyntaxError: invalid syntax
class_ = 'Advanced Theoretical Zymurgy'
print(class_)

###2.2 - expressoes e instrucoes



n = 17
print(n)
print(52)
print(n + 45)

n1 = 13
print(n1 *7)
n2 = 14
print(n2 * 7)
n3 = 15
print(n3 * 7)
n4 = 16
print(n4 * 7)
n5 = 17
print(n5 * 7)



miles = 26.2
miles * 1.61

miles = 22.2
print(miles * 1.61)
miles1 = 23.2
print(miles1 * 1.61)
miles2 = 24.2
print(miles2 * 1.61)
miles3 = 25.2
print(miles3 * 1.61)
miles4 = 26.2
print(miles4 * 1.61)

###exemplo do script

print(0)
x = 2
y = 1
z = 3
print(y)
print(x * 1)
print(z * 1)

print(0)
x1 = 2
y1 = 2
z1 = 3
print(y1)
print(x1 * 2)
print(z1 * 2)

print(0)
x2 = 3
y2 = 3
z2 = 3
print(y2)
print(x2 * 2)
print(z2 * 3)

print(0)
x3 = 4
y3 = 4
z3 = 4
print(y3)
print(x3 * 2)
print(z3 * 4)

print(32)
x = 23
print(x)

###2.2.1-introcoues de atribuicao não produz nenhuma saida

print(5)
x2 = 5
print(x2 + 1)

##ordem das operações

####expressoes de parentese


print(2*(3-1))
print(2*(3-2))
print(2*(3-3))

print((1 + 5) ** (5 - 3))
print((1 + 2) ** (5 - 2))
print((1 + 3) ** (5 - 3))
print((1 + 2) ** (5 - 3))
print((4 + 3) ** (5 - 4))
print((1 + 1) ** (4 - 1))

###calcular e gerar o resultado da quantidade de minutos

minuto0 = 20
minutes = (minuto0 * 100) / 60
print(minutes)

minuto1 = 30
minutes1 = (minuto1 * 100) / 60
print(minutes1)

minuto2 = 40
minutes2 = (minuto2 * 100) / 60
print(minutes2)

minuto3 = 50
minutes3 = (minuto3 * 100) / 60
print(minutes3)

minuto4 = 60
minutes4 = (minuto4 * 100) / 60
print(minutes4)



###exponenciação e a proxima precedencia que possui mais alta da quantidade de numero

import math
print(int(1 + math.pow(2, 2)))
print(int(2 + math.pow(2, 3)))
print(int(3 + math.pow(2, 4)))
print(int(4 + math.pow(2, 5)))
print(int(5 + math.pow(2, 6)))
print(int(6 + math.pow(2, 7)))
print(int(7 + math.pow(2, 8)))
print(int(8 + math.pow(2, 9)))
print(int(9 + math.pow(2, 10)))
print(int(10 + math.pow(2, 11)))

import math

print(int(1 + math.pow(3,2)))
print(int(2 + math.pow(3,3)))
print(int(3 + math.pow(3,4)))
print(int(4 + math.pow(3,5)))
print(int(5 + math.pow(3,6)))
print(int(6 + math.pow(3,7)))
print(int(7 + math.pow(3,8)))
print(int(8 + math.pow(3,9)))
print(int(9 + math.pow(3,10)))

import math

print(int(1 + math.pow(4,2)))
print(int(2 + math.pow(4,3)))
print(int(3 + math.pow(4,4)))
print(int(4 + math.pow(4,5)))
print(int(5 + math.pow(4,6)))
print(int(6 + math.pow(4,7)))
print(int(7 + math.pow(4,8)))
print(int(8 + math.pow(4,9)))
print(int(9 + math.pow(4,10)))

import math

print(int(1 + math.pow(5,2)))
print(int(2 + math.pow(5,3)))
print(int(3 + math.pow(5,4)))
print(int(4 + math.pow(5,5)))
print(int(5 + math.pow(5,6)))
print(int(6 + math.pow(5,7)))
print(int(7 + math.pow(5,8)))
print(int(8 + math.pow(5,9)))
print(int(9 + math.pow(5,10)))

###raiz ao quadrado

import math
print((math.sqrt(2)))
print((math.sqrt(3)))
print((math.sqrt(4)))
print((math.sqrt(5)))
print((math.sqrt(6)))
print((math.sqrt(7)))
print((math.sqrt(8)))
print((math.sqrt(9)))
print((math.sqrt(10)))

import math
print(math.sqrt(12))
print(math.sqrt(13))
print(math.sqrt(14))
print(math.sqrt(15))
print(math.sqrt(16))
print(math.sqrt(17))
print(math.sqrt(18))
print(math.sqrt(19))
print(math.sqrt(20))

import math

print(math.sqrt(21))
print(math.sqrt(22))
print(math.sqrt(23))
print(math.sqrt(24))
print(math.sqrt(25))
print(math.sqrt(26))
print(math.sqrt(27))
print(math.sqrt(28))
print(math.sqrt(29))
print(math.sqrt(30))

###calcular o valor trigonometrico seno cosseno tangente:

####seno

import math
print(math.sin(1))
print(math.sin(2))
print(math.sin(3))
print(math.sin(4))
print(math.sin(5))
print(math.sin(6))
print(math.sin(7))
print(math.sin(8))
print(math.sin(9))
print(math.sin(10))

####cosseno

import math
print(math.sin(1))
print(math.sin(2))
print(math.sin(3))
print(math.sin(4))
print(math.sin(5))
print(math.sin(6))
print(math.sin(7))
print(math.sin(8))
print(math.sin(9))
print(math.sin(10))

####tangente

import math
print(math.tan(1))
print(math.tan(2))
print(math.tan(3))
print(math.tan(4))
print(math.tan(5))
print(math.tan(6))
print(math.tan(7))
print(math.tan(8))
print(math.tan(9))
print(math.tan(10))

##elevar ao cubo + 9

#####0 ao quadrado + 9

import math
print(int(1 * math.pow(0,2)))
print(int(1 * math.pow(0,2) + 9))
print(int(1 * math.pow(0,2) + 18))
print(int(1 * math.pow(0,2) + 27))
print(int(1 * math.pow(0,2) + 36))
print(int(1 * math.pow(0,2) + 45))
print(int(1 * math.pow(0,2) + 54))
print(int(1 * math.pow(0,2) + 63))
print(int(1 * math.pow(0,2) + 72))
print(int(1 * math.pow(0,2) + 81))
print(int(1 * math.pow(0,2) + 90))

#####1 ao quadrado + 9

import math
print(int(2 * math.pow(1,2)))
print(int(2 * math.pow(1,2) + 9))
print(int(2 * math.pow(1,2) + 18))
print(int(2 * math.pow(1,2) + 27))
print(int(2 * math.pow(1,2) + 36))
print(int(2 * math.pow(1,2) + 45))
print(int(2 * math.pow(1,2) + 54))
print(int(2 * math.pow(1,2) + 63))
print(int(2 * math.pow(1,2) + 72))
print(int(2 * math.pow(1,2) + 81))
print(int(2 * math.pow(1,2) + 90))

#####2 elevado a 9

import math
print(int(2 * math.pow(2,3)))
print(int(2 * math.pow(2,3) + 9))
print(int(2 * math.pow(2,3) + 18))
print(int(2 * math.pow(2,3) + 27))
print(int(2 * math.pow(2,3) + 36))
print(int(2 * math.pow(2,3) + 45))
print(int(2 * math.pow(2,3) + 54))
print(int(2 * math.pow(2,3) + 63))
print(int(2 * math.pow(2,3) + 72))
print(int(2 * math.pow(2,3) + 81))
print(int(2 * math.pow(2,3) + 90))

#####3 elevado a 9

import math
print(int(2 * math.pow(3,3)))
print(int(2 * math.pow(3,3) + 9))
print(int(2 * math.pow(3,3) + 18))
print(int(2 * math.pow(3,3) + 27))
print(int(2 * math.pow(3,3) + 36))
print(int(2 * math.pow(3,3) + 45))
print(int(2 * math.pow(3,3) + 54))
print(int(2 * math.pow(3,3) + 63))
print(int(2 * math.pow(3,3) + 72))
print(int(2 * math.pow(3,3) + 81))
print(int(2 * math.pow(3,3) + 90))

#####4 elevado a 9

import math
print(int(2 * math.pow(4,3)))
print(int(2 * math.pow(4,3) + 9))
print(int(2 * math.pow(4,3) + 18))
print(int(2 * math.pow(4,3) + 27))
print(int(2 * math.pow(4,3) + 36))
print(int(2 * math.pow(4,3) + 45))
print(int(2 * math.pow(4,3) + 54))
print(int(2 * math.pow(4,3) + 63))
print(int(2 * math.pow(4,3) + 72))
print(int(2 * math.pow(4,3) + 81))
print(int(2 * math.pow(4,3) + 90))

#####5 elevado a 9

import math
print(int(2 * math.pow(5,3)))
print(int(2 * math.pow(5,3) + 9))
print(int(2 * math.pow(5,3) + 18))
print(int(2 * math.pow(5,3) + 27))
print(int(2 * math.pow(5,3) + 36))
print(int(2 * math.pow(5,3) + 45))
print(int(2 * math.pow(5,3) + 54))
print(int(2 * math.pow(5,3) + 63))
print(int(2 * math.pow(5,3) + 72))
print(int(2 * math.pow(5,3) + 81))
print(int(2 * math.pow(5,3) + 90))

#####6 elevado a 9

import math
print(int(2 * math.pow(6,3)))
print(int(2 * math.pow(6,3) + 9))
print(int(2 * math.pow(6,3) + 18))
print(int(2 * math.pow(6,3) + 27))
print(int(2 * math.pow(6,3) + 36))
print(int(2 * math.pow(6,3) + 45))
print(int(2 * math.pow(6,3) + 54))
print(int(2 * math.pow(6,3) + 63))
print(int(2 * math.pow(6,3) + 72))
print(int(2 * math.pow(6,3) + 81))
print(int(2 * math.pow(6,3) + 90))

##multplicação e divisão que tem a alta precedencia do que a adição e da subtração

####Exemplo 1 da multplicao e da subtracao

print(2*3-1)
print(2*3-2)
print(2*3-3)
print(2*3-4)
print(2*3-5)

####Numero sem ponto flutuante

print(int(6+0/2))
print(int(6+1/2))
print(int(6+2/2))
print(int(6+3/2))
print(int(6+4/2))
print(int(6+5/2))
print(int(6+6/2))
print(int(6+7/2))
print(int(6+8/2))
print(int(6+9/1))
print(int(6+10/2))

####Numero com ponto flutuante

print(6+1/2)
print(6+2/2)
print(6+3/2)
print(6+4/2)
print(6+5/2)
print(6+6/2)
print(6+7/2)
print(6+8/2)
print(6+9/1)
print(6+10/2)

####Esse são exemplo do livro pense em python esse exemplo são multplicação e divisão
# que tem a alta precedencia do que a adição e da subtração

print(6+5/2)

print(int(6+6/2))

print(6+7/2)

print(int(6+8/2))

###operacoes com strings

# '2'-'1'
# ----> 1 '2'-'1'
# TypeError: unsupported operand type(s) for -: 'str' and 'str'
print(str('2 - 1'))

# 'eggs'/'easy'
# ----> 1 'eggs'/'easy'
# # TypeError: unsupported operand type(s) for /: 'str' and 'str'
print(str('eggs / easy'))

# "third" * "a charm"
# ----> 1 "third" * "a charm"
# TypeError: can't multiply sequence by non-int of type 'str'
print(str('"thir" * "a charm"'))

###Ordem das operacoes

####Os parentese com a precedencia
print(2*(3-1))
print(2*(3-2))
print(2*(3-3))

print((1+1) ** (5-2))
print((1+2) ** (5-2))
print((1+3) ** (5-2))

###exponencia

print(1 + 2**3)
print(2 + 2**3)
print(3 + 2**3)

print(1 - 2 ** 3)
print(2 - 2 ** 3)
print(3 - 2 ** 3)

###Multiplicação e a divisao e a subtracao


print(2*3-(1))
print(2*3-(2))
print(2*3-(3))

###mais ha duas expressoes, + e *

first = "throat"
second = "warbler"
first + second

' spam ' * 3

###operador de multiplicacao da string

' spam ' *3

' viccenzo ' * 3

' spam ' + ' spam ' + ' spam ' * 3

print(2**2)
print(3**3)
print(4**4)
print(5**5)
print(6**6)
print(7**7)
print(8**8)
print(9**9)
print(10**10)

2**7

'spam'*3

###comentario da operacoes com a string e operador de matematica + e *

minuto3 = 60
percentage = (minuto3 * 100) / 60 #porcentage de uma hora
print(int(percentage))

n = 42
print(n)

xy = 1
(xy)

##exercicio do capitulo 2

####Exercicio 2.1

# Repetindo o meu conselho do capítulo anterior, sempre que você aprender
# um recurso novo, você deve testá-lo no modo interativo e fazer erros de
# propósito para ver o que acontece.
# • Vimos que n = 42 é legal. E 42 = n?
# • Ou x = y = 1?
# • Em algumas linguagens, cada instrução termina em um ponto e vírgula
# ;. O que acontece se você puser um ponto e vírgula no fim de uma instrução
# no Python?
# • E se puser um ponto no fim de uma instrução?
# • Em notação matemática é possível multiplicar x e y desta forma: xy. O
# que acontece se você tentar fazer o mesmo no Python?




####Exercício 2.2
# Pratique o uso do interpretador do Python como uma calculadora:
# 1. O volume de uma esfera com raio r é . Qual é o volume de uma esfera
# com raio 5?
#
# 2. Suponha que o preço de capa de um livro seja
# R$ 24,95, mas as livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o primeiro exemplar e 7
# 5 centavos para cada exemplar adicional. Qual é o custo total de atacado para 60 cópias?
#
# 3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min15s por quilômetro),
# então 3 quilômetros a um passo mais rápido (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado
# em primeiro lugar, que horas chego em casa para o café da manhã?
#

