'''
Desenvolver um programa que pergunte 3 valores (variáveis a, b e c) e ao final apresente-os dispostos em ordem
crescente.
'''

a = int(input("Insira um número inteiro:"))
b = int(input("Insira outro número inteiro:"))
c = int(input("Insira mais um número inteiro:"))

# 1- a tem que ser menor que b
if ( a > b ):
    aux = a
    a = b
    b = aux

# 2- a tem que ser menor que c
if (a > c):
    aux = a
    a = c
    c = aux

# garantido até aqui que a é o menor dos 3
# agora é necessário garantir que b seja menor que c
if (b > c):
    aux = b
    b = c
    b = aux

# garantido até aqui que entre b e c, o b é menor, ou seja, o c é o maior de todos

print(f"Ordem crescente: {a}, {b} e {c}")

'''
if a <= b and a <= c and b <= c:
    print(f'A ordem crescente é {a}, {b} e {c}')
elif a <= b and a <=c and c <= b:
    print(f'A ordem crescente é {a}, {c} e {b}')
elif b <= a and b <= c and a <= c:
    print(f'A ordem crescente é {b}, {a} e {c}')
elif b <= a and b <= c and c <= a:
    print(f'A ordem crescente é {b}, {c} e {a}')
elif c <= a and c <= b and a <=b:
    print(f'A ordem crescente é {c}, {a} e {b}')
elif c <= a and c <= b and b <= a:
    print(f'A ordem crescente é {c}, {b} e {a}')
'''