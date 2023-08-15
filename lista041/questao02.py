'''
Desenvolver um programa que permita ao aluno responder qual a capital do Brasil. O programa deverá exibir se a resposta está certa ou errada.
'''

a = str(input("Qual a capital do Brasil?"))

if (a == "Brasília" or "brasilia" or "Brasilia"):
    print("A resposta está correta!")

else:
    print("A resposta está errada!")