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

print((1,000,000,000))

print((2,000,000,000))

print((222*2,333*3,444*4,555*5,666*6,777*7,888*9,999*10))

#O resultado do capitulo 1 inteiro o exemplo eh:
# hello world
# hello world!
# meu nome é viccenzo de oliveira
# eu estou cursando o superior chamado ciência da computação
# eu sou portador de deficiência audtitiva
# eu tenho 23 ano e vou fazer 24 em junho dia 27 desse ano
# 42
# 41
# 42
# 42
# 4
# <class 'int'>
# <class 'float'>
# <class 'str'>
# <class 'str'>
# <class 'str'>
# <class 'str'>
# <class 'bool'>
# <class 'bool'>
# <class 'int'>
# <class 'int'>
# (1, 0, 0, 0)
# (2, 0, 0, 0)
# (444, 999, 1776, 2775, 3996, 5439, 7992, 9990)


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
#
#
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
