def empilha (baralho, p_origem, p_destino):
    origem = baralho [p_origem]
    destino = baralho [p_destino]
    lugar = baralho.index(destino)

    
    
    baralho [lugar] = origem
    if p_origem != 1:
        lista_para_tirar_carta = baralho [::-1]
        lista_para_tirar_carta.remove (origem)
        baralho = lista_para_tirar_carta [::-1]
    if p_origem == 1 and p_destino == 0:
        baralho.remove (origem)
    return baralho

