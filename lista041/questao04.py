'''
Desenvolver um programa que pergunte um valor numérico inteiro e faça a exibição desse valor caso seja
divisível por 4 e 5. Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem “Valor não é divisível por
4 e 5”
'''

a = int(input("Insira um número inteiro:"))

b = a%4

c= a%5

if (b==0 and c==0):
    print(f"O número {a} é divisível por 4 e 5!")

else:
    print(f"O número {a} não é divisível por 4 e 5!")