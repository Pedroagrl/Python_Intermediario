def genero():
    sexo = str(input('Qual seu sexo[M/F]: ')).upper()
    if sexo == 'M':
        print(f'O sexo escolhido foi Masculino! ')
    elif sexo == 'F':
        print(f'O sexo escolhido foi Feminino! ')
    else:
        print('Sexo invalido!')
genero()