def maior():
    n1 = int(input('Digite um numero: '))
    n2 = int(input('Digite outro numero:  '))
    n3 = int(input('O ultimo numero: '))
    maior = n1
    menor = n1
    
    if n2 > maior:
        maior = n2
    if n3 > maior:
        maior = n3
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    print(f'O maior numero digitado foi {maior} e o menor {menor}')
maior()