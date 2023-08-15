'''
Desenvolver um programa que pergunte dois valores numéricos inteiros e apresente o valor da diferença entre o
maior valor e o menor valor lido
'''

a = int(input("Insira aqui um valor inteiro:"))
b = int(input("Insira aqui outro valor inteiro:"))

if (a > b):
    print(f"A diferença entre o maior e o menor valor é de {a - b}!")

elif (a < b):
    print(f"A diferença entre o maior e o menor valor é de {b - a}!")