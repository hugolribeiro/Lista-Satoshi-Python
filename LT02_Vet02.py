# Programador: Hugo Leça Ribeiro
# Data de elaboração: 23/10/2019

# Criar e coletar um vetor [100] inteiro e exibir:
# O maior e o menor número
# A média dos valores

vet = []
maior = 0
menor = 0
media = 0
i = 0

for i in range(0, 10, 1):
    vet.append(int(input("Digite aqui um número ")))
    if i == 0:
        menor = vet[i]
        maior = vet[i]
        media = media + vet[i]
    else:
        if vet[i] < menor:
            menor = vet[i]
        if vet[i] > maior:
            maior = vet[i]
        media = media + vet[i]
media = media / 10

print("O maior número é: ", maior)
print("O menor número é: ", menor)
print("A média dos valores é: ", media)
