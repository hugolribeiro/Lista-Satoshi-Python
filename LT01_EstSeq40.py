# Objetivo: Receba 2 números inteiros. Verifique e mostre todos os números primos existentes entre eles.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 11.09.19

n1 = 0
n2 = 0
c = 0
raiz = int(0)
i = int(0)
f = 0
inv = 0

n1 = int(input("Digite o primeiro número "))
n2 = int(input("Digite o segundo número "))

if n2 < n1:
    inv = n1
    n1 = n2
    n2 = inv
if n1 <= 0:
    c = 2
else:
    c = (n1 + 1)
while c < n2:
    f = 0
    raiz = (int)(c ** 0.5)
    i = raiz
    while i > 1:
        if (c % i) == 0:
            f = (f + 1)
        i = (i - 1)
    if f == 0:
        print(c)
    c = c + 1
