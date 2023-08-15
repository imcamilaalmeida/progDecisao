'''
Desenvolver um programa que pergunte um número. Se este número for maior que 20, então ele deverá exibir a
metade deste número, senão, ele deverá exibir o número sem alterações.
'''

a = float(input("Informe um número: "))

if (a > 20):
    print(f"A metade desse número é {a/2}!")

else:
    print(f"O número é {a}!")