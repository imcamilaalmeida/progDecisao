'''
Fazer um algoritmo que peça um número, e ao final, informe se o número está abaixo de 1000, entre 1000 e
5000, entre 5001 e 8000, ou acima de 8000
'''

a = int(input("Insira um número:"))

if (a < 1000):
    print(f"O número {a} está abaixo de 1000!")

elif (a >= 1000 and a <= 5000):
    print(f"O número {a} está entre 1000 e 5000!")

else:
    if (a >= 5001 and a <= 8000):
        print(f"O número {a} está entre 5001 e 8000!")

    elif (a > 8000):
        print(f"O número {a} está acima de 8000!")