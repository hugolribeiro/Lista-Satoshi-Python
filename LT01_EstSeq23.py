# Objetivo: Receber 3 valores obrigatoriamente em ordem crescente e um 4º valor não necessariamente em ordem. Mostre os 4 números em ordem crescente.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.05.2019

print("A seguir você terá que digitar 3 números em ordem crescente, e um quarto número qualquer")
n1 = (float(input("Digite aqui o primeiro número: ")))
n2 = (float(input("Digite aqui o segundo número: ")))
n3 = (float(input("Digite aqui o terceiro número: ")))
n4 = (float(input("Digite aqui o quarto número: ")))
if (n1 < n2 < n3) and (n4 != n1) and (n4 != n2) and (n4 != n3):
    if n4 < n1:
        print("Os números em ordem crescente são1: ", n4, n1, n2, n3)
    else:
        if (n1 < n4) and (n4 < n2):
            print("Os números em ordem crescente são: ", n1, n4, n2, n3)
        else:
            if (n2 < n4) and (n4 < n3):
                print("Os números em ordem crescente são2: ", n1, n2, n4, n3)
            else:
                print("Os números em ordem crescente são3: ", n1, n2, n3, n4)
elif (n4 == n1) or (n4 == n2) or (n4 == n3):
    print("O quarto número é igual a algum outro número, digite novamente")
else:
    print("Você não digitou os três primeiros números em ordem crescente")
