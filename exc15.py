import math 

def loja_de_tintas():
    area = float(input('Tamanho da área a ser pintada(m²):  '))
    litros_necessarios = area / 6
    latas_necessarias = litros_necessarios / 18
    galoes_necessarios = litros_necessarios / 3.6
    custo_latas = latas_necessarias * 80
    custo_galoes = galoes_necessarios * 25
    print(f'{latas_necessarias:.0f} latas de 18 litros: R$ {custo_latas:.2f}')
    print(f'{galoes_necessarios:.0f} galoes de 3,6 litros: R$ {custo_galoes:.2f}')
    latas_mistas = int(litros_necessarios // 18)
    litros_restantes = litros_necessarios % 18
    galoes_mistos = math.ceil(litros_restantes / 3.6)
    custo_misto = (latas_mistas * 80) + (galoes_mistos * 25)
    print(f'{latas_mistas} latas de 18 litros e {galoes_mistos} galoes de 3,6 litros: R$ {custo_misto:.2f}')
loja_de_tintas()