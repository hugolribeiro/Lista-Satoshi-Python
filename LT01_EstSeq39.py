# Objetivo: Calcular a quantidade de grãos contidos em um tabuleiro de xadrez onde:
# Casa 1 2 3 4 ... 64
# Qtde 1 2 4 8 ... N
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 15.09.2019

c = 1
casa = 0
GraosT = 1
GraosCasaAnt = 1
graosCasaAtual = 1

casa = int(input("Digite aqui a casa desejada "))

if casa > 64 or casa <= 0:
    print("O número de casas no tabuleiro de xadrez é de 1 a 64")
else:
    while c < casa:
        graosCasaAtual = (2 * GraosCasaAnt)
        GraosT = GraosT + graosCasaAtual
        GraosCasaAnt = graosCasaAtual
        c = c + 1
    print("O número de grãos na casa atual é de: ", graosCasaAtual)
    print("O número total de grãos no tabuleiro é de: ", GraosT)
