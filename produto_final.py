import random

def cria_baralho ():
    
    paus = ['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','Q♣','J♣','K♣']
    copas = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','Q♥','J♥','K♥']
    espadas = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','Q♠','J♠','K♠']
    ouros = ['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','Q♦','J♦','K♦']
    lista_de_cartas = paus + copas + espadas + ouros
    return lista_de_cartas


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



enter = input('''Paciência Acordeão 
================== 

Seja bem-vindo(a) ao jogo de Paciência Acordeão! O objetivo deste jogo é colocar todas as cartas em uma mesma pilha. 

Existem apenas dois movimentos possíveis: 

1. Empilhar uma carta sobre a carta imediatamente anterior; 
2. Empilhar uma carta sobre a terceira carta anterior. 

Para que um movimento possa ser realizado basta que uma das duas condições abaixo seja atendida: 

1. As duas cartas possuem o mesmo valor ou 
2. As duas cartas possuem o mesmo naipe. 

Desde que alguma das condições acima seja satisfeita, qualquer carta pode ser movimentada. 

Aperte [Enter] para iniciar o jogo... ''')
if enter == '':

    baralho_aleatorio = []
    baralho = cria_baralho ()
    for k in range(len(cria_baralho())):
        tira_esse = random.choice (baralho)
        baralho_aleatorio.append (tira_esse)
        baralho.remove (tira_esse)
    
    p = True

    while p:
        f = True
        for nmr, i in enumerate (baralho_aleatorio):
            print (nmr + 1, i)
        
        escolhe = int (input ('Escolha uma carta (digite um número entre 1 e {0}): '.format (len(baralho_aleatorio))))
        while f:
            if escolhe > len(baralho_aleatorio):
                print ('Escolha um número entre 1 e {0}'.format(len(baralho_aleatorio)))
                break
            if escolhe <= len (baralho_aleatorio):
                print (baralho_aleatorio [escolhe-1])
                if possui_movimentos_possiveis(baralho_aleatorio) == True:
                    movimentos_possiveis = lista_movimentos_possiveis(baralho_aleatorio, baralho_aleatorio.index(baralho_aleatorio [escolhe-1]))
                    if movimentos_possiveis == []:
                        print ('Não há movimentos possíveis para a carta {0}, escolha outra!'.format (baralho_aleatorio [escolhe-1]))
                        f = False

                    if movimentos_possiveis == [1]:
                        baralho_aleatorio = empilha (baralho_aleatorio, escolhe-1, escolhe-2)
                        f = False
                    if movimentos_possiveis == [3]:
                        baralho_aleatorio = empilha (baralho_aleatorio, escolhe-1, escolhe-4)
                        f = False
                    if movimentos_possiveis == [1,3]:
                        decide = int(input('Escolha empilhar a carta {0} sobre: 1. {1} ou 2. {2}: '. format (baralho_aleatorio[escolhe - 1], baralho_aleatorio [escolhe - 2], baralho_aleatorio [escolhe - 4])))
                        if decide == 1:
                            baralho_aleatorio = empilha(baralho_aleatorio, escolhe-1, escolhe-2)
                            f = False
                        if decide == 2:
                            baralho_aleatorio = empilha(baralho_aleatorio, escolhe-1, escolhe-4)
                            f = False
                   
                if possui_movimentos_possiveis(baralho_aleatorio) == False:
                    print ('Não há mais movimentos possíveis no baralho, você perdeu!')
                    p = False
                    f = False