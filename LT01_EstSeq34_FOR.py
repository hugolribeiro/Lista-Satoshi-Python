# Objetivo: Receber um número. Calcular e mostrar os resultados da tabuada desse número.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 13.09.19

n = 0
i = 0
result = 0

n = int(input("Digite aqui o número para saber a tabuada: "))
for i in range(i, 11, + 1):
    result = (n * i)
    print("O resultado de ", n, "X ", i, " será: ", result)
