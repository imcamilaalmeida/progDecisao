'''
Fazer um algoritmo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final o algoritmo
deverá exibir na tela a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior
que o ano atual, o cálculo de idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela:
“Dados inseridos estão incorretos”
'''

a = int(input("Qual seu ano de nascimento?"))
b = int(input("Qual o ano atual?"))

c = b - a

if (a < b):
    print(f"A sua idade é de {c}!")

if (a > b):
    print("Dados inseridos estão incorretos!")