def caixa():
    valor = int(input('Valor do saque (Min: 10 / Max: 600): '))
    if 10 > valor > 600 :
        print('Valor inadequado!')
    total = valor
    ced = 100
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        else:
            if totced > 0:
                print(f'Total de {totced} cedulas de R$ {ced}')
            if ced == 100:
                ced = 50
            elif ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 5
            totced = 0
            if total == 0:
                break

caixa()
