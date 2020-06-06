"""
https://www.programcreek.com/2014/05/leetcode-reverse-words-in-a-string-ii-java/
Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces and the words are always separated by a single space.
For example,
Given s = "the sky is blue",
return "blue is sky the".
"""


def reverse_words(text):
    lts = text.split()
    lts.reverse()
    return ' '.join(lts)


assert reverse_words(text='the sky is blue') == 'blue is sky the'
assert reverse_words(text='The input string does not contain leading or trailing spaces') == 'spaces trailing or ' \
                                                                                             'leading contain not ' \
                                                                                             'does string input The'
