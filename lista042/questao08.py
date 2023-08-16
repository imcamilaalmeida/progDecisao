'''
Fazer um algoritmo que pergunte 3 números, e ao final, guarde na variável maior o maior destes 3 números
inseridos. O valor da variável maior deverá ser exibido ao final
'''

a = int(input("Insira um número:"))
b = int(input("Insira outro número:"))
c = int(input("Insira mais um número:"))

maior = a

if (a < b):
    maior = b

if (a < c):
    maior = c

print(f"O maior número é {maior}")