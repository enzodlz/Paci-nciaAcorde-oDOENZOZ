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

        
def lista_movimentos_possiveis (baralho, posicao):
    lugar = []
    if posicao == 0:
        return []
    for cartas in range(len(baralho)):
        if extrai_naipe(baralho[cartas]) == extrai_naipe (baralho [posicao]) and cartas == posicao - 1:
            lugar.append (1)
        if extrai_naipe(baralho[cartas]) == extrai_naipe (baralho [posicao]) and cartas == posicao - 3:
            lugar.append (3)
        if extrai_valor(baralho[cartas]) == extrai_valor (baralho [posicao]) and cartas == posicao - 1:
            lugar.append (1)                
        if extrai_valor(baralho[cartas]) == extrai_valor (baralho [posicao]) and cartas == posicao - 3:
            lugar.append (3)
    if lugar == []:
        return []

    return sorted(lugar)

print (lista_movimentos_possiveis (['6♥', 'J♥', '9♣', '9♥'], 3))