# Objetivo: Receber a quantidade de horas trabalhadas, o valor por hora, o percentual de desconto e o número de dependentes. Calcular o salário que será igual às horas trabalhadas vezes o valor por hora. Calcular o salário líquido (Salário Bruto - desconto). A cada dependente será acrescido R$ 100 no Salário Líquido. Exibir o Salário a receber.
# Programador: Hugo Leça Ribeiro
# Data de Elaboração: 04.09.2019


adicionalPorDependente = 100

hTrab = float(input("Digite aqui o total de horas trabalhadas: "))
vrPH = float(input("Digite aqui o valor da hora trabalhada: "))
percentualDeDesconto = float(input("Digite aqui o valor do desconto em porcentagem: "))
percentualDeDesconto = (percentualDeDesconto / 100)
dependentes = int(input("Digite aqui o número de dependentes: "))
salarioBruto = (hTrab * vrPH)
salarioLiq = (salarioBruto - (salarioBruto * percentualDeDesconto))
salarioAReceber = (dependentes * 100) + (salarioLiq)

print("O salário que você receberá será de: ", salarioAReceber)
