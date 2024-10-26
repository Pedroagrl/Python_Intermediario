def notas():
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    n3 = float(input('Digite sua terceira nota: '))
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        print(f'Você foi APROVADO!! Com a média de {media:.2f}')
    elif 5 <= media < 7:
        print(f'Você está de RECUPERAÇÃO!! Com a média de {media:.2f}')
    else:
        print(f'Você está REPROVADO!! Com a média de {media:.2f}')
notas()