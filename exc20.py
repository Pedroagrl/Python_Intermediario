def digitado():
    validador = str(input('Digite uma letra ou consoante: ')).upper()
    if validador == 'A' or 'I' or 'O' or 'U' or 'E':
        print(f'Você digitou a vogal {validador}')
    else:
        print(f'Você digitou a consoante {validador}')
digitado()