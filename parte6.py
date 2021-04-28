def extrai_naipe (carta):
    divide_str = [list(letra) for letra in carta]
    if len(divide_str) == 3:
        return divide_str [2] [0]
    if len(divide_str) == 2:
        return divide_str [1] [0]
        
def extrai_valor (carta):
    divide_str = [list(letra) for letra in carta]
    if len(divide_str) == 3:
        return divide_str [0] [0] + divide_str [1] [0]
    if len(divide_str) == 2:
        return divide_str [0] [0]

def possui_movimentos_possiveis (baralho):
    movimentos_possiveis = 0
    for i in range (len(baralho)):
        if extrai_naipe (baralho[i]) == extrai_naipe (baralho[i-1]) or extrai_naipe (baralho[i]) == extrai_naipe (baralho[i - 3]):
            movimentos_possiveis += 1
        if extrai_valor (baralho[i]) == extrai_valor (baralho[i-1]) or extrai_valor (baralho[i]) == extrai_valor (baralho[i - 3]):
            movimentos_possiveis += 1
        if extrai_naipe (baralho[i]) != extrai_naipe (baralho[i-1]) or extrai_naipe (baralho[i]) != extrai_naipe (baralho[i - 3]):
            movimentos_possiveis += 0
        if extrai_valor (baralho[i]) != extrai_valor (baralho[i-1]) or extrai_valor (baralho[i]) != extrai_valor (baralho[i - 3]):
            movimentos_possiveis += 0
    if movimentos_possiveis > 0:
        return True
    if movimentos_possiveis == 0:
        return False