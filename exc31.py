import math

def raizes():
    a = float(input('Digite o valor de a: '))
    if a == 0:
        print('O valor de a não pode ser zero. Esta não é uma equação do segundo grau.')
        return
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    delta = (b * b) - 4 * a * c
    if delta < 0:
        print(f'Delta negativo. A equação {delta} não possui raízes reais. ')
    elif delta == 0:
        raiz = -b / (2 * a)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2*a)
        raiz2 = (-b - math.sqrt(delta)) / (2*a)
        print(f'Delta positivo. A equação possui duas raízes reais: {raiz1:.2f} e {raiz2:.2f}')
raizes()