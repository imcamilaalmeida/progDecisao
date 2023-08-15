'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno e exiba mensagem informando que o
aluno foi aprovado se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma
mensagem informando essa condição. Apresentar junto com a mensagem de aprovação ou reprovação o valor
da média obtida pelo aluno.
'''

a = float(input("Insira a primeira nota:"))
b = float(input("Insira a segunda nota:"))
c = float(input("Insira a terceira nota:"))
d = float(input("Insira a quarta nota:"))

media = (a + b + c + d) / 4

if (media >= 5):
    print(f"Você foi aprovado. Sua média foi de {media}!")

else:
    print(f"Você foi reprovado. Sua média foi de {media}!")