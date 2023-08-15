'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente como resultado
somente o algarismo das centenas
'''

a = int(input("Insira um número inteiro de 3 algarismos: "))

b = int(a / 100)

if (a >= 100):
    print(f"O algarismo das centenas é {b}!")