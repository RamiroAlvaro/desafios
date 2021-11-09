"""Desafio Tony Lampada de la empresa Buser
   Encontrar el indice de comienzo de una palabra en un texto
   de no existir retornar -1
   por ejemplo:
   text = 'ramiro alvaro'
   word = 'alvaro'
   index_word(text, word) debe retornar 7
"""


def index_word(text, word):
    if not text and not word:
        return 0

    top_index = len(word)
    for index, _ in enumerate(text):
        if text[index: top_index] == word:
            return index
        top_index += 1
    return -1


assert index_word('', 'ramiro') == ''.find('ramiro')
assert index_word('', '') == ''.find('')
assert index_word('ramiro', '') == 'ramiro'.find('')
assert index_word('ramiro alvaro', 'alvaro') == 'ramiro alvaro'.find('alvaro')

"""
Desafio empresa Buser CamelCase
In [62]: from re import sub

In [63]: strParam = 'cats AND*Dogs-are%Awesome'

In [64]: string = sub(r"(\*|-|%)+", " ", strParam).title().replace(" ", "")

In [65]: string[0].lower() + string[1:]
Out[65]: 'catsAndDogsAreAwesome'
"""

"""
Desafio empresa Buser remove_brackets

In [42]: parentesis = ')())'

In [43]: def remove_brackets(text):
    ...:     stack = []
    ...:     for char in text:
    ...:         if stack and stack[-1] == '(' and char == ')':
    ...:             stack.pop()
    ...:         else:
    ...:             stack.append(char)
    ...:     return len(stack)
    ...:

In [44]: remove_brackets(parentesis)
Out[44]: 2

In [45]: parentesis = '(())((('

In [46]: remove_brackets(parentesis)
Out[46]: 3

In [47]: parentesis = '(())'

In [48]: remove_brackets(parentesis)
Out[48]: 0

In [49]: parentesis = '(())('

In [50]: remove_brackets(parentesis)
Out[50]: 1

In [51]: parentesis = '(()))('

In [52]: remove_brackets(parentesis)
Out[52]: 2
"""
