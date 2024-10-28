from datetime import datetime

def verificar_data(data_str):
    try:
        data = datetime.strptime(data_str, "%d/%m/%Y")
        return True
    except ValueError:
        return False

data = input('Digite uma data no formato dd/mm/aaaa:  ')
if verificar_data(data):
    print('A data é valida!')
else:
    print('A data é invalida!')