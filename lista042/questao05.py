'''
Fazer um algoritmo que pergunte a sigla de um estado brasileiro (UF -> Unidade Federativa), e ao final,
informe na tela se o estado inserido está ou não na região Sudeste.
'''

a = str(input("Insira a sigla de um estado brasileiro:"))

if (a == "RJ" or a == "rj" or a == "Rj" or a == "SP" or a == "sp" or a == "Sp" or a == "MG" or a == "mg" or a == "Mg" or a == "ES" or a == "es" or a == "Es"):
    print("O estado inserido está na Região Sudeste!")

else:
    print("O estado inserido não está na Região Sudeste!")