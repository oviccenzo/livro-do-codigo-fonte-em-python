# 4.3 - Exercícios
#
#A seguir, uma série de exercícios usando TurtleWorld. Eles servem para
#divertir, mas também têm outro objetivo. Enquanto trabalha neles,
#pense que objetivo pode ser.
#
#As seções seguintes têm as soluções para os exercícios,
#mas não olhe até que tenha terminado (ou, pelo menos, tentado).
#
# Escreva uma função chamada square que receba um parâmetro chamado t,
# que é um turtle. Ela deve usar o turtle para desenhar um quadrado.
#
#Escreva uma chamada de função que passe bob como um argumento para o
# square e então execute o programa novamente.
#
#Acrescente outro parâmetro, chamado length, ao square. Altere o corpo
# para que o comprimento dos lados seja length e então altere a chamada da
#função para fornecer um segundo argumento. Execute o programa novamente.
# Teste o seu programa com uma variedade de valores para length.
#
#Faça uma cópia do square e mude o nome para polygon.
#Acrescente outro parâmetro chamado n e altere o corpo
# para que desenhe um polígono regular de n lados.
#
#Dica: os ângulos exteriores de um polígono regular de n
#lados são 360/n graus.
#
#Escreva uma função chamada circle que use o turtle, t e um
#raio r como parâmetros e desenhe um círculo aproximado ao chamar
#polygon com um comprimento e número de lados adequados.
#Teste a sua função com uma série de valores de r.
#
#Dica: descubra a circunferência do círculo e certifique-se de que
#length * n = circumference.
#
#Faça uma versão mais geral do circle chamada arc, que
#receba um parâmetro adicional de angle, para determinar qual
#fração do círculo deve ser desenhada. angle está em unidades de graus,
# então quando angle=360, o arc deve desenhar um círculo completo.

# 4.12 - Exercícios
# Exercício 4.1
#
#Baixe o código deste capítulo no site http://thinkpython2.com/code/polygon.py.
#
# Desenhe um diagrama da pilha que mostre o estado do programa
# enquanto executa circle (bob, radius). Você pode fazer a aritmética
# à mão ou acrescentar instruções print ao código.
#
#A versão de arc na seção 4.7 - Refatoração não é muito precisa porque a
#aproximação linear do círculo está sempre do lado de fora do círculo
#verdadeiro. Consequentemente, o Turtle acaba ficando alguns píxeis de
#distância do destino correto. Minha solução mostra um modo de reduzir o
#efeito deste erro. Leia o código e veja se faz sentido para você.
#Se desenhar um diagrama, poderá ver como funciona.
#
# Exercício 4.2
#
#Escreva um conjunto de funções adequadamente geral que possa
#https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_0401.png
# desenhar flores como as da Figura 4.1.
# Figura 4.1 – Flores de tartaruga.
#
# Solução: http://thinkpython2.com/code/flower.py,
#também exige http://thinkpython2.com/code/polygon.py.

# Exercício 4.3
#
# Escreva um conjunto de funções adequadamente geral
# que possa desenhar formas como as da Figura 4.2.
# https://github.com/PenseAllen/PensePython2e/raw/master/fig/tnkp_0402.png

# Exercício 4.4
#As letras do alfabeto podem ser construídas a partir de um número
#moderado de elementos básicos, como linhas verticais e horizontais e
#algumas curvas. Crie um alfabeto que possa ser desenhado com um número
#mínimo de elementos básicos e então escreva funções que desenhem as letras.
#
#Você deve escrever uma função para cada letra, com os nomes draw_a,
#draw_b etc., e colocar suas funções em um arquivo chamado letters.py.
#Você pode baixar uma “máquina de escrever de turtle” no site
#http://thinkpython2.com/code/typewriter.py para ajudar a testar o seu código.
#
# Você pode ver uma solução no site http://thinkpython2.com/code/letters.py;
# ela também exige http://thinkpython2.com/code/polygon.py.
# Exercício 4.5
#
# Leia sobre espirais em https://pt.wikipedia.org/wiki/Espiral; então escreva um
# programa que desenhe uma espiral de Arquimedes (ou um dos outros tipos).
#
# [1] turtle graphics ou gráficos de tartaruga é o sistema de desenho popularizado
# pela linguagem Logo, onde os comandos movimentam um cursor triangular pela tela,
# conhecido como turtle ou tartaruga. A tartaruga deixa um rastro à medida que é
# movimentada, e é com esses rastros que se forma um desenho. Diferente dos sistemas
# usuais de desenho em computação gráfica, o sistema turtle graphics não exige o
# uso de coordenadas cartesianas.