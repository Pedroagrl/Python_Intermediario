def produtos():
    p1 = int(input('Preço do primeiro produto: R$'))
    p2 = int(input('Preço do segundo produto: R$'))
    p3 = int(input('Preço do terceiro produto: R$ '))
    menor = p1
    if p2 < menor:
        menor = p2
    if p3 < menor:
        menor = p3

    print(f'O produto indicado a ser comprado é o produto de preço R${menor}')
produtos()