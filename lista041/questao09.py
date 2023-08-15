'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou
nulo
'''

a = int(input("Insira um número: "))

if (a > 0):
    print(f"O número {a} é positivo!")

else:
    if (a < 0):
        print(f"O número {a} é negativo!")
    else:
        print(f"O número {a} é nulo!")