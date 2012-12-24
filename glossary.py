#-*- coding: utf8 -*-

"""
Makes glossary from text from stdin. Every 6 word translates into russian.
"""

from yandex_translate import *

translate = YandexTranslate()

import fileinput

def check(s):
    return s.lower() not in ['is','and', 'the', 'has', 'can', 'from', 'in', 'via', 'are', 'be', 'the', 'of', 'to', 'it', 'a', 'on', 'up', 'by']

words = []

for line in fileinput.input():
    for word in line.split(' '):
        if len(word)>5 and word.isalpha() and check(word) and word not in words:
            # print word
            words.append(word.lower())

for w in sorted(words[::6]):
    print w," - ", translate.translate('en-ru', w)['text'][0]
