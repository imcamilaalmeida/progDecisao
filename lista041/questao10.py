'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo
número informado é ou não um divisor do primeiro número informado
'''

a = int(input("Insira um número inteiro: "))
b = int(input("Insira outro número inteiro: "))

c = a%b

if (c == 0):
    print(f"O número {b} é divisível por {a}!")

else:
    print(f"O número {b} não é divisível por {a}!")