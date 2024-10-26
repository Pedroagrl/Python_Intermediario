def maior():
    maior = 0
    n1 = int(input('Numero 1: '))
    n2 = int(input('Numero 2: '))
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print(f'Dentre os dois numeros digitado o maior é {maior}')
maior()