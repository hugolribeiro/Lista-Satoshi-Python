# Objetivo: Receber um número. Calcular e mostrar os resultados da tabuada desse número.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 11.09.19


mult = 10
result = 0

n = float(input("Digite o número para sabermos sua tabuada "))

while mult >= 0:
    result = (mult * n)
    print("Este número vezes", mult, "resultará em ", result)
    mult -= 1
