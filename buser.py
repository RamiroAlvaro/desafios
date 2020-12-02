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
