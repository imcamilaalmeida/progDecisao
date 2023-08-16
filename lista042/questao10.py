'''
Fazer um algoritmo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá ser exibida na tela
como resposta a média do aluno, e se ele está aprovado, reprovado ou em prova final. Estas condições
devem seguir as regras da tabela abaixo:
Média Situação
Abaixo de 3,0 Reprovado
Entre 3,0 e 6,9 Prova Final
A partir de 7,0 Aprovad
'''

a = str(input("Qual seu nome?"))
b = float(input("Qual a nota da primeira prova?"))
c = float(input("Qual a nota da segunda prova?"))

d = (b + c) / 2

if (d < 3.0):
    print(f"O(a) aluno(a) {a} está reprovado(a)! Sua média é {d}.")

elif (d >= 3.0 and d <= 6.9):
    print(f"O(a) aluno(a) {a} precisará fazer a prova final! Sua média é {d}.")

else:
    if (d >= 7.0):
        print(f"O(a) aluno(a) {a} está aprovado(a)! Sua média é {d}.")