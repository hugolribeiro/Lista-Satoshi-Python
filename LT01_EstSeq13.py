# Objetivo: Receber a quantidade de alimento em quilos. Calcular e mostrar quantos dias durará esse alimento sabendo que a pessoa consome 50g ao dia.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019

quantidadeEmQuilos = float(input("Digite aqui a quantidade de alimento (em quilos): "))
duracaoDoAlimento = float(quantidadeEmQuilos * 1000 / 50)

print("Este alimento durará: ", duracaoDoAlimento, "dias")
