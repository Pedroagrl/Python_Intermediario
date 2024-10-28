def triangulos():
    lado1 = int(input('Digite o primeiro lado do triangulo: '))
    lado2 = int(input('Digite o segundo lado do triangulo: '))
    lado3 = int(input('Digite o terceiro lado do triangulo: '))

    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):

        if lado1 == lado2 == lado3:
            tipo = 'Equilatero'
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            tipo = 'Isósceles'
        else:
            tipo = 'Escaleno'
        print(f'Os lados fornecidos podem formar um triangulo {tipo}')
    else:
        print(f'Os lados fornecidos não podem formar um triangulo. ')
triangulos()