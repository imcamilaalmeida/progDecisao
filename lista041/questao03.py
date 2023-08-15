'''
 Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número é par ou
é ímpar
'''

a = int(input("Insira um número: "))

b = a%2

if (b==0):
    print(f"O número {a} é par!")

elif (b==1):
    print(f"O número {a} é ímpar!")