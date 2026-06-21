# Exercício 13.1
# Escreva um programa que leia um arquivo, quebre cada linha em palavras,
# remova os espaços em branco e a pontuação das palavras, e as converta em
# letras minúsculas.
# Dica: O módulo string oferece uma string chamada whitespace, que contém
# space, tab, newline etc., e punctuation, que contém os caracteres de
# pontuação. Vamos ver se conseguimos fazer o Python falar palavrões:
# >>> import string
# >>> string.punctuation
# ‘!"#$%&’()*+,-./:;<=>?@[\]^_`{|}~’
# Além disso, você pode usar os métodos de string, strip, replace e translate.
#
# Exercício 13.2
# Acesse o Projeto Gutenberg (http://gutenberg.org) e baixe seu livro favorito
# em domínio público em formato de texto simples.
# Altere seu programa do exercício anterior para ler o livro que você baixou,
# pulando as informações do cabeçalho no início do arquivo e processando o
# resto das palavras como antes.
# Então altere o programa para contar o número total de palavras no livro e o
# número de vezes que cada palavra é usada.
# Exiba o número de palavras diferentes usadas no livro. Compare livros
# diferentes de autores diferentes, escritos em eras diferentes. Que autor usa o
# vocabulário mais extenso?
#
# Exercício 13.3
# Altere o programa do exercício anterior para exibir as 20 palavras mais
# frequentes do livro.
#
# Exercício 13.4
# Altere o programa anterior para ler uma lista de palavras (ver “Leitura de
# listas de palavras”, na página 133) e então exiba todas as palavras do livro
# que não estão na lista de palavras. Quantas delas são erros ortográficos?
# Quantas delas são palavras comuns que deveriam estar na lista de palavras, e
# quantas são muito obscuras?
# Números aleatórios
#
# Com as mesmas entradas, a maior parte dos programas gera as mesmas saídas
# a cada vez, então eles são chamados de deterministas. Determinismo
# normalmente é uma coisa boa, já que esperamos que o mesmo cálculo
# produza o mesmo resultado. Para algumas aplicações, entretanto, queremos
# que o computador seja imprevisível. Os jogos são um exemplo óbvio, mas há
# outros.
# Fazer um programa não determinista de verdade é difícil; mas há formas de,
# pelo menos, fazê-los parecer que não são. Uma delas é usar algoritmos que
# geram números pseudoaleatórios. Os números pseudoaleatórios não são
# aleatórios mesmo porque são gerados por um cálculo determinista, mas é
# quase impossível distingui-los dos aleatórios só olhando para os números.
# O módulo random fornece funções que geram números pseudoaleatórios (que
# chamarei apenas de “aleatórios” daqui em diante).
# A função random retorna um número de ponto flutuante entre 0,0 e 1,0
# (incluindo 0,0, mas não 1,0). Cada vez que random é chamada, você recebe o
# próximo número em uma longa série. Para ver uma amostra, execute este
# loop:
# import random
# for i in range(10):
# x = random.random()
# print(x)
# A função randint recebe os parâmetros low e high e retorna um número
# inteiro entre low e high (inclusive ambos):
# >>> random.randint(5, 10)
# 5
# >>> random.randint(5, 10)
# 9
# Para escolher aleatoriamente um elemento de uma sequência, você pode usar
# choice:
# >>> t = [1, 2, 3]
# >>> random.choice(t)
# 2>>> random.choice(t)
# 3
# O módulo random também fornece funções para gerar valores aleatórios de
# distribuições contínuas, incluindo gaussianas, exponenciais, gamma e
# algumas outras.
#
# Exercício 13.5
# Escreva uma função chamada choose_from_hist que receba um histograma
# como definido em “Um dicionário como uma coleção de contadores”, na
# página 163, e retorne um valor aleatório do histograma, escolhido por
# probabilidade em proporção à frequência. Por exemplo, para este histograma:
# >>> t = [‘a’, ‘a’, ‘b’]
# >>> hist = histogram(t)
# >>> hist
# {‘a’: 2, ‘b’: 1}
# sua função deve retornar ‘a’ com a probabilidade de 2/3 e ‘b’ com a
# probabilidade 1/3.
# Histograma de palavras
# É uma boa ideia tentar fazer os exercícios anteriores antes de continuar. Você
# pode baixar minha solução em
# http://thinkpython2.com/code/analyze_book1.py. Também vai precisar de
# http://thinkpython2.com/code/emma.txt.
# Aqui está um programa que lê um arquivo e constrói um histograma das
# palavras no arquivo:
# import string
# def process_file(filename):hist = dict()
# fp = open(filename)
# for line in fp:
# process_line(line, hist)
# return hist
# def process_line(line, hist):
# line = line.replace(‘-’, ’ ’)
# for word in line.split():
# word = word.strip(string.punctuation + string.whitespace)
# word = word.lower()
# hist[word] = hist.get(word, 0) + 1
# hist = process_file(‘emma.txt’)
# Este programa lê emma.txt, que contém o texto de Emma, de Jane Austen.
# process_file faz o loop pelas linhas do arquivo, passando-as uma a uma para
# process_line. O histograma hist está sendo usado como um acumulador.
# process_line usa o método de string replace para substituir hifens por espaços
# antes de usar split para quebrar a linha em uma lista de strings. Ele atravessa
# a lista de palavras e usa strip e lower para retirar a pontuação e converter tudo
# em letras minúsculas. (Dizer que as strings “são convertidas” é uma forma
# simples de explicar a coisa; lembre-se de que as strings são imutáveis, então
# métodos como strip e lower retornam novas strings.)
# Finalmente, process_line atualiza o histograma, criando um novo item ou
# incrementando um existente.Para contar o número total de palavras no arquivo, podemos somar as
# frequências no histograma:
# def total_words(hist):
# return sum(hist.values())
# O número de palavras diferentes é somente o número de itens no dicionário:
# def different_words(hist):
# return len(hist)
# Aqui está o código para exibir os resultados:
# print(‘Total number of words:’, total_words(hist))
# print(‘Number of different words:’, different_words(hist))
# E os resultados:
# Total number of words: 161080
# Number of different words: 7214
# Palavras mais comuns
# Para encontrar as palavras mais comuns, podemos fazer uma lista de tuplas,
# onde cada tupla contenha uma palavra e a sua frequência, e ordenar a lista.
# A função seguinte recebe um histograma e retorna uma lista de tuplas de
# palavras e frequências:
# def most_common(hist):
# t = []
# for key, value in hist.items():t.append((value, key))
# t.sort(reverse=True)
# return t
# Em cada tupla, a frequência aparece primeiro, então a lista resultante é
# ordenada por frequência. Aqui está um loop que imprime as 10 palavras mais
# comuns:
# t = most_common(hist)
# print(‘The most common words are:’)
# for freq, word in t[:10]:
# print(word, freq, sep=‘\t’)
# Uso o argumento de palavra-chave sep para que print use um caractere tab
# como “separador”, em vez de um espaço, portanto a segunda coluna fica
# alinhada verticalmente. Aqui estão os resultados de Emma:
# The most common words are:
# to 5242
# the 5205
# and 4897
# of 4295
# i 3191
# a 3130
# it 2529
# herwas 2400
# she 2364
# Este código pode ser simplificado usando o parâmetro key da função sort. Se
# tiver curiosidade, pode ler sobre ele em
# https://wiki.python.org/moin/HowTo/Sorting.
# Parâmetros opcionais
# Vimos funções integradas e métodos que recebem argumentos opcionais. É
# possível escrever funções definidas pelos programadores com argumentos
# opcionais, também. Por exemplo, aqui está uma função que exibe as palavras
# mais comuns em um histograma:
# def print_most_common(hist, num=10):
# t = most_common(hist)
# print(‘The most common words are:’)
# for freq, word in t[:num]:
# print(word, freq, sep=‘\t’)
# O primeiro parâmetro é necessário; o segundo é opcional. O valor-padrão de
# num é 10.
# Se você só fornecer um argumento:
# print_most_common(hist)
# num recebe o valor-padrão. Se fornecer dois argumentos:
# print_most_common(hist, 20)
# num recebe o valor do argumento em vez disso. Em outras palavras, o
# argumento opcional ignora o valor-padrão.Se uma função tem ambos os parâmetros obrigatório e opcional, todos os
# parâmetros necessários têm que vir primeiro, seguidos pelos opcionais.
# Subtração de dicionário
# Encontrar as palavras do livro que não estão na lista de palavras de words.txt
# é um problema que você pode reconhecer como subtração de conjuntos; isto
# é, queremos encontrar todas as palavras de um conjunto (as palavras no livro)
# que não estão no outro (as palavras na lista).
# subtract recebe os dicionários d1 e d2 e devolve um novo dicionário que
# contém todas as chaves de d1 que não estão em d2. Como não nos
# preocupamos com os valores, estabelecemos todos como None:
# def subtract(d1, d2):
# res = dict()
# for key in d1:
# if key not in d2:
# res[key] = None
# return res
# Para encontrar as palavras no livro que não estão em words.txt, podemos usar
# process_file para construir um histograma para words.txt, e então subtrair:
# words = process_file(‘words.txt’)
# diff = subtract(hist, words)
# print(“Words in the book that aren’t in the word list:”)
# for word in diff:
# print(word, end=’ ’)Aqui estão alguns resultados de Emma:
# Words in the book that aren’t in the word list:
# rencontre jane’s blanche woodhouses disingenuousness
# friend’s venice apartment …
# Algumas dessas palavras são nomes e possessivos. Os outros, como
# “rencontre”, já não são de uso comum. Mas algumas são palavras comuns
# que realmente deveriam estar na lista!
#
# Exercício 13.6
# O Python fornece uma estrutura de dados chamada set, que fornece muitas
# operações de conjunto. Você pode ler sobre elas em “Conjuntos”, na página
# 274, ou ler a documentação em
# http://docs.python.org/3/library/stdtypes.html#types-set.
# Escreva um programa que use a subtração de conjuntos para encontrar
# palavras no livro que não estão na lista de palavras.
# Solução: http://thinkpython2.com/code/analyze_book2.py.
# Palavras aleatórias
# Para escolher uma palavra aleatória do histograma, o algoritmo mais simples
# é construir uma lista com várias cópias de cada palavra, segundo a frequência
# observada, e então escolher da lista:
# def random_word(h):
# t = []
# for word, freq in h.items():
# t.extend([word] * freq)
# return random.choice(t)A expressão [word] * freq cria uma lista com freq cópias da string word. O
# método extend é similar a append, exceto pelo argumento, que é uma
# sequência.
# Esse algoritmo funciona, mas não é muito eficiente; cada vez que você
# escolhe uma palavra aleatória, ele reconstrói a lista, que é tão grande quanto o
# livro original. Uma melhoria óbvia é construir a lista uma vez e então fazer
# seleções múltiplas, mas a lista ainda é grande.
# Uma alternativa é:
# 1. Usar keys para conseguir uma lista das palavras no livro.
# 2. Construir uma lista que contenha a soma cumulativa das frequências
# das palavras (veja o Exercício 10.2). O último item desta lista é o número
# total de palavras no livro, n.
# 3. Escolher um número aleatório de 1 a n. Use uma pesquisa de bisseção
# (veja o Exercício 10.10) para encontrar o índice onde o número aleatório
# seria inserido na soma cumulativa.
# 4. Usar o índice para encontrar a palavra correspondente na lista de
# palavras.
#
# Exercício 13.7
# Escreva um programa que use este algoritmo para escolher uma palavra
# aleatória do livro.
# Solução: http://thinkpython2.com/code/analyze_book3.py.
# Análise de Markov
# Se escolher palavras do livro aleatoriamente, você pode até captar certo
# sentido a partir do vocabulário, mas provavelmente não vai conseguir uma
# sentença completa:
# this the small regard harriet which knightley’s it most thingsUma série de palavras aleatórias raramente faz sentido porque não há
# nenhuma relação entre palavras sucessivas. Por exemplo, em uma sentença
# de verdade você esperaria que um artigo como “o” fosse seguido de um
# adjetivo ou um substantivo, e provavelmente não um verbo ou advérbio.
# Uma forma de medir estes tipos de relações é a análise de Markov, que
# caracteriza, para uma dada sequência de palavras, o que poderia vir a seguir,
# segundo a probabilidade. Por exemplo, a canção “Eric, the Half a Bee”
# começa assim:
# Half a bee, philosophically,
# Must, ipso facto, half not be.
# But half the bee has got to be
# Vis a vis, its entity. D’you see?
# But can a bee be said to be
# Or not to be an entire bee
# When half the bee is not a bee
# Due to some ancient injury?
# Nesse texto, a frase “half the” sempre é seguida pela palavra “bee”, mas a
# frase “the bee” pode ser seguida por “has” ou “is”.
# O resultado da análise de Markov é um mapeamento de cada prefixo (como
# “half the” e “the bee”) a todos os sufixos possíveis (como “has” e “is”).
# Com este mapeamento você pode gerar um texto aleatório, começando com
# qualquer prefixo e escolhendo a esmo entre os sufixos possíveis. Em seguida,
# você pode combinar o fim do prefixo e o novo sufixo para formar o próximo
# prefixo e repetir.
# Por exemplo, se você começar com o prefixo “Half a”, então a próxima
# palavra tem que ser “bee”, porque o prefixo só aparece uma vez no texto. Oprefixo seguinte é “a bee”, então o próximo sufixo poderia ser
# “philosophically”, “be” ou “due”.
# Neste exemplo, o comprimento do prefixo é sempre dois, mas você pode
# fazer a análise de Markov com qualquer comprimento de prefixo.
#
# Exercício 13.8
# Análise de Markov:
# 1. Escreva um programa que leia o texto de um arquivo e execute a
# análise de Markov. O resultado deve ser um dicionário que mapeie prefixos a
# uma coleção de possíveis sufixos. A coleção pode ser uma lista, tupla ou
# dicionário; você é que deverá fazer a escolha adequada. Você pode testar seu
# programa com um comprimento de prefixo 2, mas deve escrever o programa
# de forma que seja fácil testar outros comprimentos.
# 2. Acrescente uma função ao programa anterior para gerar texto aleatório
# baseado na análise de Markov. Aqui está um exemplo de Emma com o
# comprimento de prefixo 2:
# He was very clever, be it sweetness or be angry, ashamed or only
# amused, at such a stroke. She had never thought of Hannah till you were
# never meant for me?” “I cannot make speeches, Emma:” he soon cut it all
# himself.
# Para este exemplo, deixei a pontuação anexada às palavras. O resultado
# é quase sintaticamente correto, mas não exatamente. Semanticamente, quase
# faz sentido, mas não exatamente.
# O que acontece se você aumentar o comprimento dos prefixos? O texto
# aleatório faz mais sentido?
# 3. Uma vez que o seu programa esteja funcionando, você pode querer
# tentar uma mistura: se combinar o texto de dois ou mais livros, o texto
# aleatório gerado misturará o vocabulário e frases das fontes de formas
# interessantes.Crédito: este estudo de caso é baseado em um exemplo de Kernighan and
# Pike, The Practice of Programming, Addison-Wesley, 1999.
# É uma boa ideia tentar fazer este exercício antes de continuar; depois você
# pode baixar a minha solução em http://thinkpython2.com/code/markov.py.
# Também vai precisar de http://thinkpython2.com/code/emma.txt.
#
# Exercício 13.9
# A “classificação” de uma palavra é a sua posição em uma lista de palavrasclassificadas por frequência: a palavra mais comum tem a classificação 1, a
# segunda mais comum é 2 etc.
# A lei de Zipf descreve a relação entre classificações e frequências das
# palavras em linguagens naturais (http://en.wikipedia.org/wiki/Zipf ’s_law).
# Ela prevê especificamente que a frequência, f, da palavra com classificação r
# é:
# f = cr−s
# onde s e c são parâmetros que dependem do idioma e do texto. Se você tomar
# o logaritmo de ambos os lados desta equação, obtém:
# log f = log c − s log r
# Se você traçar o log de f contra o log de r, terá uma linha reta com uma
# elevação -s e interceptar o log de c.
# Escreva um programa que leia um texto em um arquivo, conte as frequências
# das palavras e exiba uma linha para cada palavra, em ordem descendente da
# frequência, com log de f e log de r. Use o programa gráfico de sua escolha
# para traçar os resultados e verifique se formam uma linha reta. Você pode
# estimar o valor de s?
# Solução: http://thinkpython2.com/code/zipf.py. Para executar a minha
# solução, você vai precisar do módulo de tracejamento matplotlib. Se você
# instalou o Anaconda, já tem o matplotlib; se não tiver, é preciso instalá-lo.