def crime2():
    lista_perguntas = []
    lista_perguntas.append(str(input('Telefonou para vitima?[S/N] ')).upper())
    lista_perguntas.append(str(input('Esteve no local do crime?[S/N] ')).upper())
    lista_perguntas.append(str(input('Mora perto da vitima?[S/N] ')).upper())
    lista_perguntas.append(str(input('Devia para a vitima?[S/N] ')).upper())
    lista_perguntas.append(str(input('Ja trabalhou com a vitima?[S/N] ')).upper())
     
    participacao2 = 0

    for c in lista_perguntas:
        if c == "S":
            participacao2 += 1

    if participacao2 == 2:
        classificacao = "Suspeita"
    elif participacao2 in [3,4]: 
        classificacao = "Cumplice"
    elif participacao2 == 5:
        classificacao = "Assasino"
    else:
        classificacao = "Inocente"

    print(f"Você respondeu {participacao2} perguntas positivamente e é classificada como {classificacao}")

    print(f"")
crime2()
