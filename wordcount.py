"""
13. wordcount
Este desafio é um programa que conta palavras de um arquivo qualquer de duas
formas diferentes.
A. Lista todas as palavras por ordem alfabética indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --count letras.txt
Ele deve imprimir todas as palavras em ordem alfabética seguidas
do número de ocorrências.
Por exemplo:
$ python wordcount.py --count letras.txt
a 2
b 4
c 3
B. Lista as 20 palavras mais frequêntes indicando suas ocorrências.
Ou seja...
Dado um arquivo letras.txt contendo as palavras: A a C c c B b b B
Quando você executa o programa: python wordcount.py --topcount letras.txt
Ele deve imprimir as 20 palavras mais frequêntes seguidas
do número de ocorrências, em ordem crescente de ocorrências.
Por exemplo:
$ python wordcount.py --topcount letras.txt
b 4
c 3
a 2
Abaixo já existe um esqueleto do programa para você preencher.
Você encontrará a função main() chama as funções print_words() e
print_top() de acordo com o parâmetro --count ou --topcount.
Seu trabalho é implementar as funções print_words() e depois print_top().
"""

import sys
from collections import Counter


def order_by_quantity(word_qty):
    word, qty = word_qty
    return qty, word


def read_and_count(filename):
    with open(filename, 'rt') as f:
        data = f.read()
    words = data.lower().split()
    return list(Counter(words).items())


def print_words(filename):
    words_qty = read_and_count(filename)
    words_qty.sort()
    return '\n'.join(f'{word} {qty}' for word, qty in words_qty)


def print_top(filename, limit=20):
    words_qty = read_and_count(filename)
    words_qty.sort(key=order_by_quantity, reverse=True)
    return '\n'.join(f'{word} {qty}' for word, qty in words_qty[:limit])


def main():
    if len(sys.argv) != 3:
        print('Utilização: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print(print_words(filename))
    elif option == '--topcount':
        print(print_top(filename))
    else:
        print('unknown option: ' + option)
        sys.exit(1)


if __name__ == '__main__':
    main()
