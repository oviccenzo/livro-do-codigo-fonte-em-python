#Capitulo 1: jornada do programa

##1.3 -primeiro programa

print("hello world")

print('hello world!')

print('meu nome é viccenzo de oliveira')
print('eu estou cursando o superior chamado ciência da computação')
print('eu sou portador de deficiência audtitiva')
print('eu tenho 23 ano e vou fazer 24 em junho dia 27 desse ano')

##1.4 operadores aritmeticos

print(40 + 2)

print(43-2)

print(6*7)

print((6**2) + 6)

print(6 ^ 2)

##1.5 - valores e tipos

print(type(2))

print(type(42.0))

print(type('hello world!'))

print(type('2'))

print(type('42.0'))

print(type('hello world!'))

print(type(True))

print(type(False))

print(type(229))

print(type(32*2))

(1,000,000,000)

(2,000,000,000)

(222*2,333*3,444*4,555*5,666*6,777*7,888*9,999*10)

##exercicio do capitulo 1

####Exercicio 1.1

# É uma boa ideia ler este livro em frente a um computador para testar os
# exemplos durante a leitura.
# Sempre que estiver testando um novo recurso, você deve tentar fazer erros.
# Por exemplo, no programa “Hello, World!”, o que acontece se omitir uma das
# aspas? E se omitir ambas? E se você soletrar a instrução print de forma
# errada?
# Este tipo de experimento ajuda a lembrar o que foi lido; também ajuda
# quando você estiver programando, porque assim conhecerá o significado das
# mensagens de erro. É melhor fazer erros agora e de propósito que depois e
# acidentalmente.
# 1. Em uma instrução print, o que acontece se você omitir um dos
# parênteses ou ambos?
# 2. Se estiver tentando imprimir uma string, o que acontece se omitir uma
# das aspas ou ambas?
# 3. Você pode usar um sinal de menos para fazer um número negativo
# como -2. O que acontece se puser um sinal de mais antes de um número? E se
# escrever assim: 2++2?4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02.
# O que acontece se você tentar usar isso no Python?
# 5. O que acontece se você tiver dois valores sem nenhum operador entre
# eles?


# 1. Em uma instrução print, o que acontece se você omitir um dos parênteses ou ambos?
# print "Hello, World!" # Isso causaria um SyntaxError no Python 3 (sintaxe do Python 2)
# print("Hello, World!" # Isso causaria um SyntaxError: unexpected EOF while parsing
print("1. Omitir um parêntese ou ambos na função print() no Python 3 causa um SyntaxError.")

# 2. Se estiver tentando imprimir uma string, o que acontece se omitir uma das aspas ou ambas?
# print(Hello, World!) # Isso causaria um NameError: name 'Hello' is not defined
# print("Hello, World!) # Isso causaria um SyntaxError: EOL while scanning string literal
print("2. Omitir aspas ao imprimir uma string causará um NameError (se for uma palavra ",
      "não definida) ou um SyntaxError (se a string não for fechada corretamente).")

# 3. Você pode usar um sinal de menos para fazer um número negativo como -2.
#O que acontece se puser um sinal de mais antes de um número? E se escrever assim: 2++2?
print(f"3. Um sinal de mais antes de um número é permitido: {+2}")
print(f"3. Escrever 2++2 é interpretado como 2 + (+2): {2++2}")

# 4. Na notação matemática, zeros à esquerda são aceitáveis, como em 02.
#O que acontece se você tentar usar isso no Python?
# print(02) # Isso causaria um SyntaxError: invalid decimal literal
#em Python 3.8+ ou SyntaxError: leading zeros in
# decimal integer literals are not permitted; use an 0o prefix for octal integers
print("4. Zeros à esquerda em números (como 02) causam um SyntaxError no Python 3",
      "Eles seriam interpretados como octal em versões antigas ou requerem um prefixo 0o.")

# 5. O que acontece se você tiver dois valores sem nenhum operador entre eles?
# print(2 2) # Isso causaria um SyntaxError: invalid syntax
print("5. Dois valores sem um operador entre eles (por exemplo, '2 2') causam um SyntaxError.")

####Exercicio 1.2

# Exercício 1.2
# Inicialize o interpretador do Python e use-o como uma calculadora.
# 1. Quantos segundos há em 42 minutos e 42 segundos?
# 2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a
# 1,61 quilômetro.
# 3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o
# seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua
# velocidade média em milhas por hora?


# 1. Quantos segundos há em 42 minutos e 42 segundos?
minutes = 42
seconds = 42
total_seconds = (minutes * 60) + seconds
print(f"1. Em 42 minutos e 42 segundos há: {total_seconds} segundos")

# 2. Quantas milhas há em 10 quilômetros? Dica: uma milha equivale a 1,61 quilômetro.
distance_km = 10
km_per_mile = 1.61
distance_miles = distance_km / km_per_mile
print(f"2. Em 10 quilômetros há: {distance_miles:.2f} milhas")

# 3. Se você correr 10 quilômetros em 42 minutos e 42 segundos, qual é o
# seu passo médio (tempo por milha em minutos e segundos)? Qual é a sua velocidade média em milhas por hora?

# Converter distância para milhas
distance_km_run = 10
miles_run = distance_km_run / km_per_mile

# Converter tempo total para segundos
time_minutes_run = 42
time_seconds_run = 42
total_time_seconds_run = (time_minutes_run * 60) + time_seconds_run

# Calcular passo médio (tempo por milha em minutos e segundos)
pac_minutes_per_mile = (total_time_seconds_run / 60) / miles_run
pac_whole_minutes = int(pac_minutes_per_mile)
pac_remaining_seconds = (pac_minutes_per_mile - pac_whole_minutes) * 60
print(f"3.a. Seu passo médio é de: {pac_whole_minutes} minutos e {pac_remaining_seconds:.0f} segundos por milha")

# Calcular velocidade média em milhas por hora
total_time_hours_run = total_time_seconds_run / 3600
speed_mph = miles_run / total_time_hours_run
print(f"3.b. Sua velocidade média é de: {speed_mph:.2f} milhas por hora")

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

print(42)

n = 17 *22

print(n)

print(n + 25 ** 2)

n1 = 17
print(n1)

miles = 26.2
miles * 1.61

miles = 26.2
print(miles * 1.61)

###exemplo do script

print(1)
x = 2
print(x)

print(32)
x1 = 23
print(x1)

###2.2.1-introcoues de atribuicao não produz nenhuma saida

print(5)
x2 = 5
print(x2 + 1)

##ordem das operações

####expressoes de parentese

print(2*(3-1))

print((1 + 1) ** (5 - 2))

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

####Esse são exemplo do livro pense em python esse exemplo
# são multplicação e divisão que tem a alta precedencia do que a adição e da subtração

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


#### Exercicio 2.2

# Pratique o uso do interpretador do Python como uma calculadora:
# 1. O volume de uma esfera com raio r é . Qual é o volume de uma esfera
# com raio 5?
# 2. Suponha que o preço de capa de um livro seja R$ 24,95, mas as
# livrarias recebem um desconto de 40%. O transporte custa R$ 3,00 para o
# primeiro exemplar e 75 centavos para cada exemplar adicional. Qual é o
# custo total de atacado para 60 cópias?
# 3. Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo
# passo (8min15s por quilômetro), então 3 quilômetros a um passo mais rápido
# (7min12s por quilômetro) e 1 quilômetro no mesmo passo usado em primeiro
# lugar, que horas chego em casa para o café da manhã?




# Capitulo 3: funcoes

###3.1 - chamada de função usando o type , int, str, o type eh para identificar o numero e palavra
# e o int usado para mostrar o valor sem o ponto flutuante e o float mostrar varios ponto flutuante

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

####a mesma composição do codigo anterior usando a função integrada são aplicada a
# função definidas pelos programadores, então podemos usar qualquer tipo de expressão como argumentos

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

###Exercicio 3.2
# Um objeto de função é um valor que pode ser atribuído a uma variável ou
# passado como argumento. Por exemplo, do_twice é uma função que toma umobjeto
# de função como argumento e o chama duas vezes:
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

#


#Capitulo 5: Condicionais e recursividade

##Divisão pelo piso e módulo

#### divisao individual que seria esse simbolo /

minutes = 105
print(minutes / 60)
minutes1 = 110
print(minutes1 / 60)
minutes2 = 115
print(minutes2 / 60)
minutes3 = 120
print(minutes3 / 60)
minutes4 = 125
print(minutes4 / 60)
minutes5 = 130
print(minutes5 / 60)


#### divisão dupla //

minutes = 105
print(minutes // 60)
minutes1 = 110
print(minutes1 // 60)
minutes2 = 115
print(minutes2 // 60)
minutes3 = 120
print(minutes3 // 60)
minutes4 = 125
print(minutes4 // 60)
minutes5 = 130
print(minutes5 // 60)

#### modulo %

minutes = 105
print(minutes % 60)
minutes1 = 110
print(minutes1 % 60)
minutes2 = 115
print(minutes2 % 60)
minutes3 = 120
print(minutes3 % 60)
minutes4 = 125
print(minutes4 % 60)
minutes5 = 130
print(minutes5 % 60)

minutes6 = 105
print(minutes6 / 60)

minutes7 = 105
hours = minutes7 // 60
print(hours)

### Esse programa é usado para pode obter o resto e subtrair hora em minuto

minutes8 = 105
hours = minutes8 // 60
remainder = minutes8 - hours * 60
print(remainder)

minutes9 = 110
hours1 = minutes9 // 60
remainder1 = minutes9 - hours1 * 60
print(remainder1)

minutes10 = 105
remainder2 = minutes10 % 60
print(remainder2)

minutes11 = 110
remainder3 = minutes11 % 60
print(remainder3)

##Expressões booleanas

print(5 == 5)

print(5 == 6)

print(type(True))

print(type(False))

x = 3
y = 1
print(x != y) # x não é igual a y

y1 = 9
print(x > y1) # x é maior que y

y2 = 23
print(x < y2) # x é menor que y

y3 = 2
print(x >= y3) # x é maior ou igual a y

y4 = 3
print(x <= y4) # x é menor ou igual a y

##Operadores logicos


####operador and

x1 = 9
print(x1 > 0 and x1 < 10)

####operador or

n1 = 90

print(n1 % 2 == 0 or n1 % 3 == 0 )

###numero % 2 igual a zero ou numero % 3 igual a zero for True or False

n = int(input("Digite um numero inteiro: "))
n1 = int(input("Digite um numero inteiro: "))

print(f"O numero eh verdadeiro ou falso: {n % 2 == 0 or n1 % 3 == 0}")

print(42 and True)

print(42 and False)

print(42 or False)

##Execução condicional

#### execução condicional

x2 = int(input("Digite qualquer número: "))

if x2 > 0:
  print("x é positivo")
elif x2 < 0:
  print("x é negativo")

x3 = 4

if x3 < 0:
  pass

print(x3)

#### execução alternativa

x4 = int(input("Digite qualquer número: "))

if x4 % 2 == 0:
  print("x is even")
else:
  print("x is odd")

#### condição encadeadas

x5 = int(input("Digite qualquer número: "))
y5 = int(input("Digite qualquer número: "))

if x5 < y5:
  print("x is less than y")
elif x5 > y5:
  print("x is greater than y")
else:
  print("x and y are equal")

choice = input("Digite a letra a, b ou c: ")
draw_a = 1
draw_b = 2
draw_c = 3

if choice == 'a':
  draw_a()
elif choice == 'b':
  draw_b()
elif choice == 'c':
  draw_c()

print(f"O resultado desse exemplo eh: {choice}")

####Condição aninhadas

x7 = int(input("Digite qualquer número: "))
y7 = int(input("Digite qualquer número: "))

if x7 == y7:
  print("x and y are equal")
else:
  if x7 < y7:
    print("x is less than y")
  else:
    print("x is greater than y")

x8 = int(input("Digite qualquer número: "))

if 0 < x8:
  if x8 < 10:
    print("x is a positive single-digit number")

x9 = int(input("Digite qualquer número: "))

if 0 < x9 and x9 < 10:
  print("x is a positive single-digit number")

x10 = int(input("Digite qualquer número: "))

if 0 < x10 < 10:
  print("x is a positive single-digit number")


####Execução alternativa

x6 = int(input("Digite qualquer número: "))

if x6 % 2 == 0:
  print("x is even")
else:
  print("x is odd")

#### Recursividade

def countdown(n):
  if n <= 0:
    print("Blastoff!")
  else:
    print(n)
    countdown(n-1)

countdown(10)

def countdown1(n1):
  return n1

countdown1(3)

# # A função `countdown` é um exemplo clássico de **função recursiva**, o
#  que significa que ela chama a si mesma para resolver um problema. A ideia
# central da recursividade é dividir um problema em versões menores e mais simples
# do mesmo problema, até chegar a um caso básico que pode ser resolvido diretamente.
# #
# Vamos analisar a função e a execução de `countdown(3)`:

# ```python
# def countdown(n):
#   if n <= 0:
#     print("Blastoff!")
#   else:
#     print(n)
#     countdown(n-1) # Chamada recursiva
# ```

# ### Como a função funciona:

# 1.  **Caso Base (`if n <= 0`):**
#     *   Este é o ponto de parada da recursão. Se `n` for `0` ou
# negativo, a função imprime "Blastoff!" e não chama mais a si mesma. Isso é crucial para
# evitar um loop infinito.

# 2.  **Passo Recursivo (`else`):**
#     *   Se `n` for maior que `0`, a função faz duas coisas:
#         a.  Imprime o valor atual de `n`.
#         b.  Chama a si mesma (`countdown(n-1)`) com um argumento `n-1`, ou
# seja, o problema se torna um pouco menor a cada chamada.

# ### Traço de Execução para `countdown(3)`:

# *   **1. `countdown(3)` é chamada:**
#     *   `n` é `3` (maior que 0).
#     *   Imprime: `3`
#     *   Chama: `countdown(2)`

# *   **2. `countdown(2)` é chamada:**
#     *   `n` é `2` (maior que 0).
#     *   Imprime: `2`
#     *   Chama: `countdown(1)`

# *   **3. `countdown(1)` é chamada:**
#     *   `n` é `1` (maior que 0).
#     *   Imprime: `1`
#     *   Chama: `countdown(0)`

# *   **4. `countdown(0)` é chamada:**
#     *   `n` é `0` (igual a 0).
#     *   Imprime: `Blastoff!`
#     *   **Retorna** (aqui a recursão começa a "desempilhar").

# *   **5. `countdown(1)` retorna:**
#     *   A execução volta para onde `countdown(0)` foi chamada. Não há mais
# código na função `countdown(1)` para executar, então ela **retorna**.

# *   **6. `countdown(2)` retorna:**
#     *   Similarmente, a execução volta para onde `countdown(1)` foi chamada.
# `countdown(2)` também **retorna**.

# *   **7. `countdown(3)` retorna:**
#     *   Finalmente, `countdown(3)` retorna, e o controle volta para a parte do código que chamou
# `countdown(3)` inicialmente.

# ### Saída Total:
# ```
# 3
# 2
# 1
# Blastoff!
# ```

# Em resumo, a recursividade é uma técnica poderosa onde uma função resolve um
# problema chamando a si mesma com versões menores do problema até atingir um caso base, e
#  então as soluções das sub-chamadas são combinadas.

def countdown2(n2):
  if n2 <= 0:
    print("Blastoff!")
  else:
    print(n2)
    countdown2(n-1)

if __name__ == '__main__':
  countdown(3)

def countdown3(n3):
  return n3

countdown3(3)

n3 = 2
n4 = 0
if n3  > n4:
  print(n3)
  countdown3(n3-1)
  countdown3(n4-2)

def countdown4(n5):
  return n5

countdown4(3)

def countdown5(n6):
  return n6

countdown5(2)

n6 = 1
n7 = 0
if n6  > n7:
  print(n6)
  countdown3(n7-1)
print(countdown5(n7))

def countdown6(n8):
  return n8

countdown6(2)

def countdown7(n9):
  return n9

countdown7(1)

n9 = 0
n10 = 1
if n9  > n10:
  print(n9)
  countdown(n9-1)
print(countdown7(n9))
print(countdown7(n10))

####Recursividade infinita

# def recurse():
#   return recurse()

# recurse()

## entrada do teclado

text = input() #what are you wating for

text1 = input() #what are you training for?

name = input("What... is your name?\n")
#what are you wating for
# arthur, king of the britons

name

prompt = "what...is the airspeed velocity of an unladen swallow?\n"
speed = input(prompt)

int(speed)

# prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
# speed1 = input(prompt1)
# int(speed1)
# 1 prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
      # 2 speed1 = input(prompt1)
# ----> 3 int(speed1)

# ValueError: invalid literal for int() with base 10: 'What do you mean, an African or a European swallow?'
# mostra esse sinal de erro  prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
      # 2 speed1 = input(prompt1)
# ----> 3 int(speed1)
      # 4 # 1 prompt1 = "what...is the airspeed velocity of an unladen swallow?\n"
      # 5       # 2 speed1 = input(prompt1)

# ValueError: invalid literal for int() with base 10: 'int(speed1)'


# Capitulo 6 Funções com resultado

##Valores de retorno

import math

radians3 = float(input("Digite qualquer número: "))
radius = float(input("Digite qualquer número: "))
expoente = float(input("Digite qualquer número: "))


e = math.exp(expoente)
height = radius * math.sin(radians3)

print(f"O valor dor resultado do expoente de e eh: {e}")
print(f"O valor do resultado radius eh: {height}")

import math

def area(radius4):
  a = math.pi * radius4**2
  return a

radius4 = float(input("Digite qualquer número de radius: "))
print(f"O valor do resultado eh: {area(radius4)}")

import math

def area1(radius5):
  return math.pi * radius5 ** 2

radius5 = float(input("Digite qualquer número de radius: "))
print(f"O valor do resultado eh: {area1(radius5)}")

##Variavies temporais e o valor absoluto

def absolute_value(x6):
  if x6 < 0:
    return -x6
  else:
    return x6

x6 = float(input("Digite qualquer número: "))
print(f"O valor absolute eh: {absolute_value(x6)}")

def absolute_value1(x7):
  if x7 < 0:
    return -x7
  if x7 > 0:
    return x7
absolute_value1(0)

print(absolute_value1(0))

##Desenvolvimento incremental

#####calcular dois ponto dados pelas coordenada

def distancia(x12, y12, x13, y13):
  return 0.0

distancia(1, 2, 4, 6)

def distancia1(x14,y14,x15,y15):
  dx = x14 - x15
  dy = y14 - y15
  print(f"dx is {dx}")
  print(f"dy is {dy}")
  return 0.0

distancia1(1,2,4,6)

import math

def distancia2(x16,y16,x17,y17):
  dx = x16 - y17
  dy = y16 - y17
  dsquared = dx**2 + dy**2
  print(f"dsquared is: {dsquared}")
  return
distancia2(1,2,4,5)

import math

def distancia3(x18,y18,x19,y19):
  dx1 = x18 - y19
  dy1 = y18 - y19
  dsquared1 = dx1 ** 2 + dy1 ** 2
  result = math.sqrt(dsquared1)
  return result

distancia3(1,2,4,6)

##Composição

####Calcular area do circulo e o ponto no perimetro

import math

def area2(radius6):
  radius6 = float(input("Digite qualquer numero: "))
  return math.pi * radius6 ** 2

def circle_area(xc, yc, xp, yp):
  radius6 = distancia(xc, yc, xp, yp)
  result = area2(radius6)
  return result

circle_area(1,2,4,6)

import math
def area3 (radius7):
  return math.pi * radius7 ** 2

def circle_area1(xc1,xy1,xp1,yp1):
  radius7 = distancia1(xc1,xy1,xp1,yp1)


##Funções booleanos

####Retornando a funções booleanos

def is_divisible(x19, y19):
  if x19 % y19 == 0:
    return True
  else:
    return False

print(is_divisible(6,4))
print(is_divisible(6,3))

def is_divisible1(x20, y20):
  return x20 % y20 == 0
print(is_divisible1(6,4))
print(is_divisible1(6,3))

###Funções booleanos incondicionais

def is_divisible2(x21,y21):
  print("x is divisible by y")
  return x21 % y21 == 0

print(is_divisible2(6,4))
print(is_divisible2(6,3))

def is_divisible3(x22,y22):
  if x22 % y22 == True:
    print("x is divisible by y")

def is_between(x,y,z):
  return x <= y <= z

print(is_between(8,9,11))

##Mais recursividade

def factorial(n):
  if n == 0:
    return 1
  else:
    recurse = factorial(n-1)
    result3 = n * recurse
    return result3

print(factorial(5))
print(factorial(6))
print(factorial(7))
print(factorial(8))



# Capitulo 7: Iteração

x16 = 1
x16

x17 = 7
x17

# Capitulo 8: Strings




# Capitulo 9 estudos de caso: jogos de palavras



# Capitulo 10: Lista



# Capitulo 11: Dicionarios



# Capitulo 12: Tuplas



# Capitulo 13: estudos de caso: selecao de estrutura de dados



# Capitulo 14: arquivos



# Capitulos 15: Classes e objetos



# Capitulo 16: Classes e funcoes



# Capitulo 17: Classes e metodos



# Capitulo 18: Herança



# Capitulo 19: Extra



#capitulo 20: Depuração


####Loop infinito

x11 = int(input("Digite qualquer numero: "))
y11 = int(input("Digite qualquer numero: "))

while x11 > 0 and y11 < 0:
  print("x: ", x11)
  print("y: ", y11)
  print("condition: ",(x11 > 0 and y11 < 0))

#capitulo 21:Análises de algoritmo



# Eu pedir para o gemini me auxiliar e me explicar sobre como entender analise de algoritmo

text_answer = """
Exercício 21.1 - Notação Grande-O (Big-Oh notation)

Aqui estão as respostas e o raciocínio para cada pergunta, baseado nos princípios da Notação Grande-O:

1.  **Qual é a ordem de crescimento de n^3 + n^2? E de 1000000n^3 + n^2? Ou de n^3 + 1000000n^2?**
    *   **Princípio:** A notação Big-O foca no termo de maior crescimento 
    (termo dominante) à medida que 'n' se aproxima do infinito. Coeficientes constantes e termos de menor ordem são desconsiderados.

    *   **n^3 + n^2:** O termo dominante é n^3.
        *   **Ordem de crescimento:** O(n^3)

    *   **1000000n^3 + n^2:** O termo dominante é n^3. O coeficiente 1000000 
    não altera a ordem de crescimento assintótica.
        *   **Ordem de crescimento:** O(n^3)

    *   **n^3 + 1000000n^2:** O termo dominante é n^3, pois n^3 
    cresce muito mais rápido que n^2, mesmo com um grande coeficiente.
        *   **Ordem de crescimento:** O(n^3)

2.  **Qual é a ordem de crescimento de (n^2 + n) . (n + 1)? Antes de começar a
 multiplicar, lembre-se de que você só precisa do termo principal.**
    *   **Princípio:** Para produtos de funções, você pode multiplicar os termos dominantes de cada fator.

    *   **Termos dominantes:** O termo dominante de (n^2 + n) é n^2. O termo dominante de (n + 1) é n.
    *   **Multiplicação dos termos dominantes:** n^2 * n = n^3.
    *   **Ordem de crescimento:** O(n^3)
    *   (Se você expandir completamente, terá n^3 + 2n^2 + n, cujo termo dominante é n^3).

3.  **Se f está em O(g), para alguma função não especificada g, o que podemos dizer de af+b?**
    *   **Princípio:** Coeficientes constantes e termos de menor ordem não afetam 
    a ordem de crescimento de uma função no contexto Big-O.
    *   **Resposta:** Se f(n) está em O(g(n)), então a função af(n) + b também está em **O(g(n))**.
        *   Isso ocorre porque 'a' é uma constante multiplicativa e 'b' é uma constante aditiva 
        (ou um termo de ordem menor se for uma função constante), e a notação Big-O é sobre o comportamento 
        assintótico para grandes 'n', onde esses fatores se tornam insignificantes em comparação com o termo dominante.

4.  **Se f1 e f2 estão em O(g), o que podemos dizer a respeito de f1 + f2?**
    *   **Princípio:** Se duas funções têm a mesma ordem de crescimento, 
    a soma delas também terá essa ordem de crescimento.
    *   **Resposta:** Se f1(n) está em O(g(n)) e f2(n) está em O(g(n)), então f1(n) + f2(n) está em **O(g(n))**.
        *   Por exemplo, se f1(n) = 3n e f2(n) = 5n, ambas são O(n). f1(n) + f2(n) = 8n, que também é O(n).

5.  **Se f1 está em O(g) e f2 está em O(h), o que podemos dizer a respeito de f1 + f2?**
    *   **Princípio:** A ordem de crescimento da soma de duas funções é dominada pela função 
    com a maior taxa de crescimento.
    *   **Resposta:** Se f1(n) está em O(g(n)) e f2(n) está em O(h(n)), então f1(n) + f2(n) 
    está em **O(max(g(n), h(n)))**.
        *   Isso significa que você pega a função de maior complexidade entre g(n) e h(n). 
        Por exemplo, se g(n) = n e h(n) = n^2, então f1(n) + f2(n) seria O(n^2).

6.  **Se f1 está em O(g) e f2 é O(h), o que podemos dizer a respeito de f1 . f2?**
    *   **Princípio:** A ordem de crescimento do produto de duas funções é o produto de suas ordens de crescimento.
    *   **Resposta:** Se f1(n) está em O(g(n)) e f2(n) está em O(h(n)), então f1(n) * f2(n) está em **O(g(n) * h(n))**.
        *   Por exemplo, se f1(n) = O(n) e f2(n) = O(n^2), então f1(n) * f2(n) seria O(n * n^2) = O(n^3).
"""

# Para exibir a resposta, você pode simplesmente imprimir a string:
print(text_answer)


### Exemplos Práticos da Notação Big-O

# Vamos usar o Python para visualizar como as funções crescem e como os princípios da Notação Big-O se aplicam.

# Para a questão 1: Ordem de crescimento de n^3 + n^2, 1000000n^3 + n^2, n^3 + 1000000n^2

import matplotlib.pyplot as plt
import numpy as np

def f1(n): return n**3 + n**2
def f2(n): return 1000000 * n**3 + n**2
def f3(n): return n**3 + 1000000 * n**2

def g_n3(n): return n**3 # A função de referência O(n^3)

n_values = np.arange(1, 20) # Pequenos valores de n para visualização

plt.figure(figsize=(12, 8))

plt.plot(n_values, f1(n_values), label='f1(n) = n^3 + n^2')
plt.plot(n_values, f2(n_values), label='f2(n) = 1000000n^3 + n^2')
plt.plot(n_values, f3(n_values), label='f3(n) = n^3 + 1000000n^2')
plt.plot(n_values, g_n3(n_values) * 1000000, 
         linestyle='--', color='black', label='C * n^3 (para comparação)') # Multiplicar C para que seja visível

plt.title('Crescimento de Funções e Termo Dominante')
plt.xlabel('n')
plt.ylabel('Valor da Função')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0) # Começar y em 0
plt.show()

print("Mesmo com coeficientes grandes, para n suficientemente grande, o termo dominante (n^3) prevalece.")
print("Para todas as funções acima, a ordem de crescimento é O(n^3).")

#### Explicação da Questão 1 (Código):

# Neste gráfico, observamos três funções que, à primeira vista, podem parecer 
# muito diferentes devido aos seus coeficientes. No entanto, o conceito de Big-O nos diz para focar 
# no termo que cresce mais rapidamente quando `n` se torna muito grande.

# - `f1(n) = n^3 + n^2`: O termo dominante é `n^3`.
# - `f2(n) = 1000000n^3 + n^2`: O termo dominante ainda é `n^3`. O coeficiente `1000000` 
# apenas estica a função verticalmente, mas não muda a sua forma fundamental de crescimento cúbico.
# - `f3(n) = n^3 + 1000000n^2`: Aqui, embora `1000000n^2` pareça grande para pequenos `n`, 
# `n^3` eventualmente superará `n^2` (mesmo com o coeficiente). Por exemplo, para `n=1000`, 
# `n^3` é `10^9`, enquanto `1000000n^2` é `10^6 * 10^6 = 10^12`. Ah, peraí! O `n^3` é `10^9`, e `1000000 * n^2` é 
# `10^6 * (10^3)^2 = 10^6 * 10^6 = 10^12`. Meu exemplo numérico estava errado. `10^12` é maior que `10^9`. 
# Então, para `n=1000`, `1000000n^2` domina. Mas a partir de qual `n` o `n^3` se torna dominante?

# Vamos recalcular para f3(n):
# `n^3` vs `1000000n^2`
# Dividindo por `n^2` (para `n > 0`):
# `n` vs `1000000`
# Então, para `n > 1000000`, o termo `n^3` se torna dominante. Para os pequenos valores de `n` no gráfico, 
# o termo `1000000n^2` é quem domina. Isso reforça a importância do "para n suficientemente grande".
# 
# O gráfico mostra que todas as funções seguem o padrão de crescimento de `n^3`, mesmo que `f2` e 
# `f3` sejam escaladas verticalmente. A linha tracejada preta (C * n^3) serve para ilustrar que,
# com uma constante `C` adequada, o comportamento das funções pode ser limitado por `n^3`.
# 
# **Conclusão para Q1:** Todas as funções têm ordem de crescimento **O(n^3)**.

# Para a questão 2: Ordem de crescimento de (n^2 + n) . (n + 1)

import matplotlib.pyplot as plt
import numpy as np

def h1(n): return (n**2 + n) * (n + 1)
def h_n3(n): return n**3

n_values = np.arange(1, 20) # Pequenos valores de n para visualização

plt.figure(figsize=(10, 6))

plt.plot(n_values, h1(n_values), label='h1(n) = (n^2 + n) * (n + 1)')
plt.plot(n_values, h_n3(n_values), linestyle='--', color='red', label='h_n3(n) = n^3 (termo dominante)')

plt.title('Crescimento de Produto de Funções')
plt.xlabel('n')
plt.ylabel('Valor da Função')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.show()

print("O termo dominante de (n^2 + n) é n^2.")
print("O termo dominante de (n + 1) é n.")
print("Multiplicando os termos dominantes (n^2 * n), obtemos n^3.")
print("Portanto, a ordem de crescimento de (n^2 + n) . (n + 1) é O(n^3).")

#### Explicação da Questão 2 (Código):

# Quando lidamos com o produto de funções, a regra simplificada da Notação 
# Big-O nos permite multiplicar os termos dominantes de cada fator.
# 
# - Para `(n^2 + n)`, o termo dominante é `n^2`.
# - Para `(n + 1)`, o termo dominante é `n`.

# Ao multiplicar esses termos dominantes (`n^2 * n`), obtemos `n^3`. 
# O gráfico confirma que a função `(n^2 + n) * (n + 1)` cresce de forma similar a 
# `n^3`, pois a linha da função `h1(n)` acompanha de perto a linha de `n^3`.

# **Conclusão para Q2:** A ordem de crescimento é **O(n^3)**.
# 
# Vamos agora para as questões 3, 4, 5 e 6, que tratam mais das propriedades 
# da notação Big-O com composição e adição/multiplicação de funções.

# Para a questão 3: Se f está em O(g), o que podemos dizer de af+b?

import matplotlib.pyplot as plt
import numpy as np

def g(n): return n**2
def f_example(n): return 5 * n**2 + 10 * n + 50 # Um exemplo de f em O(g)
def af_plus_b(n): return 2 * f_example(n) + 100 # a=2, b=100

n_values = np.arange(1, 20)

plt.figure(figsize=(10, 6))

plt.plot(n_values, f_example(n_values), label='f(n) = 5n^2 + 10n + 50 (Exemplo de O(n^2))')
plt.plot(n_values, af_plus_b(n_values), label='af(n) + b (2 * f(n) + 100)')
plt.plot(n_values, g(n_values) * 10, linestyle='--', color='red', label='C * g(n) = 10n^2 (para comparação de O(n^2))')

plt.title('Efeito de Constantes em O(g)')
plt.xlabel('n')
plt.ylabel('Valor da Função')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.show()

print("Se f(n) está em O(g(n)), isso significa que para n suficientemente grande, f(n) <= C "
      "* g(n) para alguma constante C.")
print("Quando aplicamos af(n) + b, o termo 'a' apenas escala f(n) e 'b' adiciona uma constante.")
print("No comportamento assintótico, essas constantes não mudam a ordem de crescimento fundamental.")
print("Portanto, se f está em O(g), então af + b também está em O(g).")

#### Explicação da Questão 3 (Código):

# O Big-O é sobre o comportamento assintótico, ou seja, o que acontece com a função quando `n` 
# se torna muito, muito grande. Constantes multiplicativas (`a`) e aditivas (`b`) não alteram a 
# forma como a função cresce a longo prazo.
# 
# No exemplo, `f_example(n)` é `O(n^2)`. Quando calculamos `af_plus_b(n)`, que é `2 * f_example(n) + 100`, 
# o gráfico mostra que ela ainda mantém o mesmo padrão de crescimento quadrático, apenas é um pouco mais alta. 
# A linha `C * g(n)` (que é `10 * n^2`) demonstra que a função `af_plus_b` ainda pode ser limitada por 
# uma versão escalada de `g(n)`.
# 
# **Conclusão para Q3:** Se `f` está em `O(g)`, então `af + b` também está em **O(g)**.

# Para a questão 4: Se f1 e f2 estão em O(g), o que podemos dizer a respeito de f1 + f2?

import matplotlib.pyplot as plt
import numpy as np

def g_qn4(n): return n**2
def f1_qn4(n): return 3 * n**2 + 5 * n
def f2_qn4(n): return 2 * n**2 + 10
def sum_f1_f2_qn4(n): return f1_qn4(n) + f2_qn4(n)

n_values = np.arange(1, 20)

plt.figure(figsize=(10, 6))

plt.plot(n_values, f1_qn4(n_values), label='f1(n) = 3n^2 + 5n (O(n^2))')
plt.plot(n_values, f2_qn4(n_values), label='f2(n) = 2n^2 + 10 (O(n^2))')
plt.plot(n_values, sum_f1_f2_qn4(n_values), label='f1(n) + f2(n)')
plt.plot(n_values, g_qn4(n_values) * 5, linestyle='--', color='red', 
         label='C * g(n) = 5n^2 (para comparação de O(n^2))')

plt.title('Soma de Funções com Mesma Ordem de Crescimento')
plt.xlabel('n')
plt.ylabel('Valor da Função')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.show()

print("Se f1 e f2 estão ambas em O(g), significa que ambas são limitadas superiormente por g(n).")
print("A soma delas, f1 + f2, também será limitada superiormente por g(n) (possivelmente com uma constante maior).")
print("Portanto, se f1 e f2 estão em O(g), então f1 + f2 também está em O(g).")

#### Explicação da Questão 4 (Código):

# Quando somamos duas funções que têm a mesma ordem de crescimento Big-O 
# (ambas `O(g)`), o resultado da soma também terá a mesma ordem de crescimento.
# 
# No exemplo, `f1_qn4(n)` (`3n^2 + 5n`) é `O(n^2)` e `f2_qn4(n)` (`2n^2 + 10`) 
# também é `O(n^2)`. A soma `f1_qn4(n) + f2_qn4(n)` resulta em `5n^2 + 5n + 10`, que, como esperado, 
# é `O(n^2)`. O gráfico mostra que a soma segue o mesmo padrão de crescimento quadrático.
# 
# **Conclusão para Q4:** Se `f1` e `f2` estão em `O(g)`, então `f1 + f2` também está em **O(g)**.

# Para a questão 5: Se f1 está em O(g) e f2 está em O(h), o que podemos dizer a respeito de f1 + f2?

import matplotlib.pyplot as plt
import numpy as np

def g_qn5(n): return n # O(n)
def h_qn5(n): return n**2 # O(n^2)
def f1_qn5(n): return 5 * n + 2 # Exemplo de O(n)
def f2_qn5(n): return 2 * n**2 + 10 * n # Exemplo de O(n^2)
def sum_f1_f2_qn5(n): return f1_qn5(n) + f2_qn5(n)

n_values = np.arange(1, 20)

plt.figure(figsize=(10, 6))

plt.plot(n_values, f1_qn5(n_values), label='f1(n) = 5n + 2 (O(n))')
plt.plot(n_values, f2_qn5(n_values), label='f2(n) = 2n^2 + 10n (O(n^2))')
plt.plot(n_values, sum_f1_f2_qn5(n_values), label='f1(n) + f2(n)')
plt.plot(n_values, h_qn5(n_values) * 2.5, 
         linestyle='--', color='red', label='C * h(n) = 2.5n^2 (para comparação de O(n^2))')

plt.title('Soma de Funções com Diferentes Ordens de Crescimento')
plt.xlabel('n')
plt.ylabel('Valor da Função')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.show()

print("Quando somamos funções com diferentes ordens de crescimento, a ordem da soma é "
      "dominada pela função de crescimento mais rápido.")
print("Neste caso, O(n^2) é uma ordem de crescimento maior que O(n).")
print("Portanto, se f1 está em O(g) e f2 está em O(h), então f1 + f2 está em O(max(g, h)).")

#### Explicação da Questão 5 (Código):

# Quando somamos funções com ordens de crescimento diferentes, a função resultante terá a ordem de crescimento 
# da função que cresce mais rapidamente. Isso é conhecido como a regra do `max`.

# No exemplo:
# - `f1_qn5(n)` (`5n + 2`) é `O(n)`.
# - `f2_qn5(n)` (`2n^2 + 10n`) é `O(n^2)`.
# 
# A soma `f1_qn5(n) + f2_qn5(n)` resulta em `2n^2 + 15n + 2`. O termo dominante é `2n^2`, 
# o que significa que a soma é `O(n^2)`. O gráfico ilustra claramente que `f1 + f2` segue o padrão de 
# crescimento de `n^2`, que é a ordem mais alta entre `O(n)` e `O(n^2)`.
# 
# **Conclusão para Q5:** Se `f1` está em `O(g)` e `f2` está em `O(h)`, então `f1 + f2` está em **O(max(g, h))**.

# Para a questão 6: Se f1 está em O(g) e f2 é O(h), o que podemos dizer a respeito de f1 . f2?

import matplotlib.pyplot as plt
import numpy as np

def g_qn6(n): return n # O(n)
def h_qn6(n): return n**2 # O(n^2)
def f1_qn6(n): return 3 * n # Exemplo de O(n)
def f2_qn6(n): return 4 * n**2 # Exemplo de O(n^2)
def prod_f1_f2_qn6(n): return f1_qn6(n) * f2_qn6(n)
def gh_qn6(n): return g_qn6(n) * h_qn6(n) # O(n * n^2) = O(n^3)

n_values = np.arange(1, 20)

plt.figure(figsize=(10, 6))

plt.plot(n_values, f1_qn6(n_values), label='f1(n) = 3n (O(n))')
plt.plot(n_values, f2_qn6(n_values), label='f2(n) = 4n^2 (O(n^2))')
plt.plot(n_values, prod_f1_f2_qn6(n_values), label='f1(n) * f2(n)')
plt.plot(n_values, gh_qn6(n_values) * 12, linestyle='--', 
         color='red', label='C * g(n) * h(n) = C * n^3 (para comparação de O(n^3))')

plt.title('Produto de Funções com Diferentes Ordens de Crescimento')
plt.xlabel('n')
plt.ylabel('Valor da Função')
plt.legend()
plt.grid(True)
plt.ylim(bottom=0)
plt.show()

print("Quando multiplicamos funções, as ordens de crescimento Big-O são multiplicadas.")
print("Neste caso, O(n) * O(n^2) resulta em O(n^3).")
print("Portanto, se f1 está em O(g) e f2 está em O(h), então f1 . f2 está em O(g . h).")

#### Explicação da Questão 6 (Código):

# Para o produto de duas funções, a ordem de crescimento resultante é o produto das ordens de crescimento individuais.

# No exemplo:
# - `f1_qn6(n)` (`3n`) é `O(n)`.
# - `f2_qn6(n)` (`4n^2`) é `O(n^2)`.
# 
# O produto `f1_qn6(n) * f2_qn6(n)` é `(3n) * (4n^2) = 12n^3`. 
# Como esperado, a ordem de crescimento é `O(n^3)`. O gráfico mostra que o produto
# das duas funções (`f1(n) * f2(n)`) segue o mesmo padrão de crescimento de `n^3`.
# 
# **Conclusão para Q6:** Se `f1` está em `O(g)` e `f2` está em `O(h)`, então `f1 . f2` está em **O(g . h)**.

#Exercicio pratica

numeros = [1,2,3,4,5,6,7,8,9]
numeros1 = [10,11,12,13,14,15,16,17,18]
resultado = []
x = 3

for numero in numeros:
  resultado.append(numero * x)

for numero1 in numeros1:
  resultado.append(numero1 * x)

print(resultado)

minute = float(input("Digite qualquer numero minuto: "))

porcentagem = (minute * 100) / 60 #% minute

print(f"A porcentagem de minuto eh: {porcentagem:.4f} %")

st = 'Ola word'
len(st)

st1 = 'Ola mundo velho ' + "ola mundo novo" + "meu nome eh viccenzo omwjfjdfl"
len(st1)
