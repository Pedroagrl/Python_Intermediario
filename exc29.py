def notas():
    n1 = float(input('Primeira nota: '))
    n2 = float(input('Segunda nota: '))
    media = (n1 + n2) / 2
    if 9.0 <= media < 10.0:
        conceito = 'A'
    elif 7.5 <= media < 9.0:
        conceito = 'B'
    elif 6.0 <= media < 7.5:
        conceito = 'C'
    elif 4.0 <= media < 6.0:
        conceito = 'D'
    elif 0.0 <= media < 4.0:
        conceito = 'E'
    else:
        print('Valor invalido')
    
    print(f'A média do aluno é: {media:.2f}')
    print(f'O conceito do aluno é: {conceito} ')
notas()