#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово. Добавить к нему в начале четыре символа «+»
# и в конце – пять символов «–»

if __name__ == '__main__':
    word = str(input("Введите слово "))
    word = '+'*4 + word + '-'*5
    print(word)
