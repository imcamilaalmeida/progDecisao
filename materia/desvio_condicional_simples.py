'''
Crie um programa que pergunte dois numeros ao usuario.
Em seguida o programa deverá somar os dois números e
apresentar o resultado se o valor for maior que 10.
'''

num1 = int(input("Informe um número:"))
num2 = int(input("Informe outro número:"))

soma = num1 + num2

print("")

if (soma > 10):
    print(f"O resultado da soma é igual a {soma}")
    print("")

elif (soma == 10):
    print(f"O resultado da soma é igual a {soma}")
    print("")

else:
    print("O resultado é menor que 10!")
    print("")

print("FIM DO PROGRAMA!")