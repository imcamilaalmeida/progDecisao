'''
Fazer um algoritmo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou
abaixo de 1000
'''

a = int(input("Insira um número:"))

if (a < 1000):
    print(f"O número {a} é menor que 1000!")

elif (a > 1000):
    print(f"O número {a} é maior que 1000!")