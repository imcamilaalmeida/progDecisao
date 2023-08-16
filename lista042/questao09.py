'''
Fazer um algoritmo que pergunte a idade de uma pessoa, e ao final, informe na tela se a pessoa é menor de
idade, se é maior de idade, ou se é maior de 65 anos
'''

a = int(input("Qual a sua idade?"))

if (a < 18):
    print("Você é menor de idade!")

elif (a >= 18 and a < 65):
    print("Você é maior de idade!")

else:
    if (a >= 65):
        print("Você está na terceira idade!")