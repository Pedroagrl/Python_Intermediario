def semana():
    dias={
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sabado '
    }
    while True:
        numero = int(input('Digite um número de 1 a 7 para representar o dia da semana: '))
        if numero in dias:
            print(f'O dia correspondente é: {dias[numero]}')
            break
        else:
            print('Valor invalido!')
semana()