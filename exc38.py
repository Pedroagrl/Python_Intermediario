def verificaçao(numero):
    if numero % 2 == 0:
        paridade = "par"
    else:
        paridade = "impar"
    
    if numero > 0:
        sinal = "positivo"
    elif numero < 0:
        sinal = "negativo"
    else:
        sinal = "neutro"
    
    if numero == int(numero):
        tipo = "inteiro"
    else:
        tipo = "decimal"
    
    return paridade, sinal, tipo


numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
operacao = input("Escolha uma operação (+, -, *): ")


if operacao == "+":
    resultado = numero1 + numero2
elif operacao == "-":
    resultado = numero1 - numero2
elif operacao == "*":
    resultado = numero1 * numero2
else:
    resultado = "Operação inválida."

if isinstance(resultado, (int,float)):
    paridade, sinal, tipo = verificaçao(resultado)
    print(f"O resultado da operação é: {resultado}")
    print(f"O resultado é {paridade}, {sinal} e {tipo}")
else:
    print(resultado)