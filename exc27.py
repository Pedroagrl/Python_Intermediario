def trabalho():
    horas = int(input('Horas trabalhadas: '))
    horas_salarial = float(input('Ganho por hora: '))
    salario = horas * horas_salarial
    if salario <= 900:
        print('Seu salario não sofre a taxação do imposto de renda!')
    if  900 <= salario <= 1500:
        imposto = (salario * 5/100) 
        print(f'Seu salario tem que pagar o imposto de renda de 5% ficando por R${imposto}')
    if 1500 <= salario <= 2500:
        imposto = (salario * 10/100)
        print(f'Seu salario tem que pagar o imposto de renda de 10% ficando por R${imposto}')
    if salario >= 2500:
        imposto = (salario * 20/100)
        print(f'Seu salario tem que pagar o imposto de renda de 20% ficando por R${imposto}')
trabalho()