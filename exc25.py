def turno():
    turnos = str(input('Qual turno você estuda? [M/V/N] ')).upper()
    if turnos == 'M':
        print('Bom dia')
    elif turnos == 'V':
        print('Boa tarde')
    elif turnos == 'N':
        print('Boa noite')
    else:
        print('Valor Invalido!')
turno()