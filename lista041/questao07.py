'''
Desenvolver um programa que pergunte um valor inteiro positivo ou negativo, e exiba como resposta o módulo
deste valor, ou seja, o número lido como sendo positivo
'''

a = int(input("Insira um número inteiro positivo ou negativo: "))

if (a < 0):
    print(f"O módulo do número é {a * -1}!")

else:
    print(f"O módulo do número é {a}!")