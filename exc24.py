def lista():
    numeros = []
    for c in range(1,6):
        numero = int(input(f'Digite o {c}º numero:  '))
        numeros.append(numero)
        numeros.sort(reverse=True)
    print(numeros)
lista()