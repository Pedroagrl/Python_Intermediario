kg = float(input('Kilogramas de peixe: '))
multa = (kg - 50) * 4
if kg < 50:
    print(f'Você comprou {kg}kgs de peixe e não vai pagar uma multa excedente')
else:
    print(f'Você comprou {kg}kgs de peixe e vai pagar uma multa excedente de {multa}R$')