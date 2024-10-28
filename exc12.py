altura = float(input('Altura(m):  '))
sexo = str(input('Sexo [H/M]: ')).upper()
pesoh = (72.7 * altura) - 58
pesom = (62.1 * altura) - 44.7
if sexo == 'H':
    print(f'O seu peso ideal é {pesoh:.2f}')
else:
    print(f'O seu peso ideal é {pesom:.2f}')