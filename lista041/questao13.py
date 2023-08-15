'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Insira um número inteiro:"))
b = int(input("Insira outro número inteiro:"))
c = int(input("Insira mais um número inteiro:"))

maior = a

if (maior < b):
    maior = b

if (maior < c):
    maior = c

menor = a

if (menor > b):
    maior = b

if (menor > c):
    maior = c

medio = a

if (medio < menor and medio < maior):
    medio = b

if (maior < c):
    maior = c