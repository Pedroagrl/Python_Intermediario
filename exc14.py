hora = float(input('Ganho por hora: R$'))
trabalhadas = int(input('Horas trabalhadas mensalmente: '))
salario = hora * trabalhadas
inss = salario * 0.08
sindicato = salario * 0.05
imposto = salario * 0.11
liquido = (salario) - (inss + sindicato + imposto)
print(f'Você trabalha {trabalhadas} horas e tem o salario bruto de R${salario}.')
print(f'Valor dos impostos de renda: R${imposto}.')
print(f'Valor do INSS pago mensalmente R${inss}.')
print(f'Valor do sindicato: R${sindicato}')
print(f'Valor do salario liquido: R${liquido}')
