def contador(numero):
    if numero >= 1000:
        return "O numero deve ser menor que 1000"

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    resultado = f"{numero} = "
    if centenas > 0:
        resultado += f"{centenas} centena(s)"
    if dezenas > 0:
        if centenas > 0:
            resultado += ", "
        resultado += f"{dezenas} dezena(s)"
    if unidades > 0:
        if centenas > 0 or dezenas > 0:
            resultado += " e "
        resultado += f"{unidades} unidade(s)"
    return resultado

numero_input = int(input("Digite um numero inteiro maior que 1000: "))
print(contador(numero_input))