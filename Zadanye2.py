#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано слово из 12 букв. Переставить в обратном порядке буквы, расположенные между
# второй и десятой буквами (т.е. с третьей по девятую).

if __name__ == '__main__':
    word = input("Введите слово из 12 букв ")
    word = word.replace(word[2], word[8], 1)
    word = word.replace(word[3], word[7], 1)
    word = word.replace(word[4], word[6], 1)
    print(word)