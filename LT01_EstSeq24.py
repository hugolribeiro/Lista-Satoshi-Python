# Objetivo: Receber um valor inteiro. Verificar se é divisível por 2 e 3.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 05.09.2019

n1 = float(input("Digite aqui um número: "))
testePor2 = n1 % 2
testePor3 = n1 % 3

if (testePor2 == 0) and (testePor3 == 0):
    print("Este número é divisível por 2 e por 3")
elif (testePor2 == 0) and (testePor3 != 0):
    print("Este número é divisível por 2, mas não por 3")
elif (testePor2 != 0) and (testePor3 == 0):
    print("Este número é divisível por 3, mas não por 2")
elif (testePor2 != 0) and (testePor3 != 0):
    print("Este número não é divisível por 3 nem por 2")
