'''
Fazer um algoritmo que peça um número de 1 a 7, e ao final, informe o dia da semana (por extenso)
correspondente ao número que foi inserido. Informar também a mensagem “número inválido” quando o
número inserido não corresponder à um dia da semana
'''

a = int(input("Insira um número de 1 a 7:"))

lista = [1, 2, 3, 4, 5, 6, 7]

if (a == 1):
    print("O dia da semana é Domingo!")

elif (a == 2):
    print("O dia da semana é Segunda-Feira!")

else:
    if (a == 3):
        print("O dia da semana é Terça-Feira!")

    elif (a == 4):
        print("O dia da semana é Quarta-Feira!")

    else:
        if (a == 5):
            print("O dia da semana é Quinta-Feira!")

        elif (a == 6):
            print("O dia da semana é Sexta-Feira!")

        else:
            if (a == 7):
                print("O dia da semana é Sábado!")

            elif (a != lista):
                print("Por favor, insira um número válido!")