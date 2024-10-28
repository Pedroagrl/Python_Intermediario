def posto():
    combustivel = str(input('Encher tanque com Gasolina ou Alcool? [G/A]: ')).upper()
    litros = int(input('Quantos litros: '))

    if combustivel == "G":
        if litros <= 20:
            desconto = (litros * 2.5) * 96/100
        else:
            desconto = (litros * 2.5) * 94/100 
    elif combustivel == "A":
        if litros <= 20:
            desconto = (litros * 1.9) * 97/100
        else:
            desconto = (litros * 1.9) * 95/100
    else:
        print('Use apenas [G] ou [A]. ')
        return
    
    print(f"O preço a pagar é R${desconto:.2f} pelos {litros} litros.")

posto()