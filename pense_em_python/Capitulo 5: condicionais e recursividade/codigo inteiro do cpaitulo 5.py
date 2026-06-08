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


# Exercícios
# Exercício 5.1
# O módulo time fornece uma função, também chamada time, que devolve a
# Hora Média de Greenwich na “época”, que é um tempo arbitrário usado
# como ponto de referência. Em sistemas UNIX, a época é primeiro de janeiro
# Comentário de 1970.
# >>> import time
# >>> time.time()
# 1437746094.5735958
# Escreva um script que leia a hora atual e a converta em um tempo em horas,
# minutos e segundos, mais o número de dias desde a época.
# Exercício 5.2
# O último teorema de Fermat diz que não há nenhum número inteiro positivo
# a, b e c tal que
# an + bn = cn
# para quaisquer valores de n maiores que 2.
# 1. Escreva uma função chamada check_fermat que receba quatro
# parâmetros – a, b, c e n – e verifique se o teorema de Fermat se mantém. Se n
# for maior que 2 e
# an + bn = cn
# o programa deve imprimir, “Holy smokes, Fermat was wrong!” Senão o
# programa deve exibir “No, that doesn’t work.”
# 2. Escreva uma função que peça ao usuário para digitar valores para a, b,
# c e n, os converta em números inteiros e use check_fermat para verificar se
# violam o teorema de Fermat.
# Exercício 5.3
# Se você tiver três gravetos, pode ser que consiga arranjá-los em um triângulo
# ou não. Por exemplo, se um dos gravetos tiver 12 polegadas de comprimento
# e outros dois tiverem uma polegada de comprimento, não será possível fazer
# com que os gravetos curtos se encontrem no meio. Há um teste simples para
# Os seguintes exercícios usam o módulo turtle, descrito no Capítulo 4:
# Exercício 5.5
# Leia a próxima função e veja se consegue compreender o que ela faz (veja os
# exemplos no Capítulo 4). Então execute-a e veja se acertou.
# def draw(t, length, n):
# if n == 0:
# return
# angle = 50
# t.fd(length*n)
# t.lt(ângulo)
# draw(t, length, n-1)
# t.rt(2*angle)
# draw(t, length, n-1)
# t.lt(ângulo)
# t.bk(length*n)
# Figura 5.2 – Uma curva de Koch.
# Exercício 5.6
# A curva de Koch é um fractal que parece com o da Figura 5.2. Para desenhar
# uma curva de Koch com o comprimento x, tudo o que você tem que fazer é:
# 1. Desenhe uma curva de Koch com o comprimento x/3.
# 2. Vire 60 graus à esquerda.
# 3. Desenhe uma curva de Koch com o comprimento x/3.
# 4. Vire 120 graus à direita.
# 5. Desenhe uma curva de Koch com o comprimento x/3.
# 6. Vire 60 graus à esquerda.
# 7. Desenhe uma curva de Koch com o comprimento x/3.
# A exceção é se x for menor que 3: neste caso, você pode desenhar apenas
# uma linha reta com o comprimento x.
# 1. Escreva uma função chamada koch que receba um turtle e um
# comprimento como parâmetros, e use o turtle para desenhar uma curva de
# Koch com o comprimento dado.
# 2. Escreva uma função chamada snowflake que desenhe três curvas de
# Koch para fazer o traçado de um floco de neve.
# Solução: http://thinkpython2.com/code/koch.py.
# 3. A curva de Koch pode ser generalizada de vários modos. Veja
# exemplos em http://en.wikipedia.org/wiki/Koch_snowflake e implemente o
# seu favorito.
# Comentário