'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
'''

a = int(input("Insira um número inteiro:"))

if (a >= 1 and a <= 10):
    print(f"O número {a} está entre 1 e 10!")

else:
    print(f"O número {a} não está entre 1 e 10!")