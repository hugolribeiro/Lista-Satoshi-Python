# Objetivo: Calcular e mostrar a série 1 – 2/4 + 3/9 – 4/16 + 5/25 ... + 15/225
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 19.09.2019

num = 0
den = 0
result = 0

while abs(num) < 15:
    if num % 2 == 0:
        num = (-(num)) + 1
    else:
        num = (-(num)) - 1
    den = (num ** 2)
    result = result + (num / den)
print(result)
