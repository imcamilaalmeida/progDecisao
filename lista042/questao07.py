'''
Fazer um algoritmo que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e qual é
o menor, ou ainda, se ambos são iguais
'''

a = int(input("Insira um número:"))
b = int(input("Insira outro número:"))

if (a == b):
    print("Os dois números são iguais!")

elif (a > b):
    print(f"O número {a} é o maior e o número {b} é o menor!")

else:
    if (a < b):
        print(f"O número {b} é o maior e o número {a} é o menor!")