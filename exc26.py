def reajuste():
    salario = float(input('Salario atual: R$'))
    if salario <= 280:
        aumento = (salario * 20/100) + salario
        print(f'Com o aumento, seu novo salario será R${aumento}! Recebendo um aumento de 20%')
    if 280 < salario <= 700:
        aumento = (salario * 15/100) + salario
        print(f'Com o aumento, seu novo salario será R${aumento}! Recebendo um aumento de 15%')
    if 700 < salario < 1500:
        aumento = (salario * 10/100) + salario
        print(f'Com o aumento, seu novo salario será R${aumento}! Recebendo um aumento de 10%')
    if salario >= 1500:
        aumento = (salario * 5/100) + salario
        print(f'Com o aumento, seu novo salario será R${aumento}! Recebendo um aumento de 5%')
reajuste()