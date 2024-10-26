def verificar_numero(numero):
    if numero == int(numero):
        return "O numero é inteiro"
    else:
        return "O numero é decimal"
numero_input = input("Digite um numero: ")

try:
    numero = float(numero_input)
    resultado = verificar_numero(numero)
    print(resultado)
except ValueError:
    print("A entrada não é um numero valido! ")