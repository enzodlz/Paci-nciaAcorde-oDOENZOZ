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


def lista_movimentos_possiveis(baralho, posicao):
    
    cartas = baralho [posicao]
    naipe = extrai_naipe(cartas)
    valor = extrai_valor(cartas)
    
    movimentos = []
    if posicao >= 3:

        carta_1 = baralho[posicao - 1]
        naipe_1 = extrai_naipe(carta_1)
        valor_1 = extrai_valor(carta_1)

        if naipe == naipe_1 or valor == valor_1:
            movimentos.append(1)
        carta_2 = baralho[posicao - 3]
        naipe_2 = extrai_naipe(carta_2)
        valor_2 = extrai_valor(carta_2)

        if naipe == naipe_2 or valor == valor_2:
            movimentos.append(3)
            
    elif posicao >= 1:

        carta_3 = baralho[posicao - 1]
        naipe_3 = extrai_naipe(carta_3)
        valor_3 = extrai_valor(carta_3)
        
        if naipe == naipe_3 or valor == valor_3:
            movimentos.append(1)
    return sorted (movimentos)


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
    
    for i in range(len(baralho)):

        movimentos = lista_movimentos_possiveis(baralho, i)

        if movimentos != []:
            return True
            
    return False


class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m' #RESET COLOR

def colore_baralho (carta):
    if extrai_naipe(carta) == '♣':
        return bcolors.WARNING + "{0}".format(carta) + bcolors.RESET
    if extrai_naipe(carta) == '♥':
        return bcolors.FAIL + "{0}".format(carta) + bcolors.RESET
    if extrai_naipe(carta) == '♠':
        return carta
    if extrai_naipe(carta) == '♦':
        return bcolors.OKBLUE + "{0}".format(carta) + bcolors.RESET

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

        if possui_movimentos_possiveis(baralho_aleatorio) == True:
            f = True
            for nmr, i in enumerate (baralho_aleatorio):
                printa = nmr + 1
                printa1 = i
                print (bcolors.OK + "{0}".format(printa) + bcolors.RESET + ' ' + colore_baralho (printa1))
            
            
            while f:
                escolhe = input ('Escolha uma carta (digite um número entre 1 e {0}): '.format (len(baralho_aleatorio)))
                if not escolhe.isdigit():
                    print("Digite apenas numeros!")
                if escolhe.isdigit():
                    escolhe = int (escolhe)
                    if escolhe > len(baralho_aleatorio):
                        print (bcolors.FAIL + 'Escolha um número entre 1 e {0}!'.format(len(baralho_aleatorio))+ bcolors.RESET)
                        
                    if escolhe <= len (baralho_aleatorio):
                        print (baralho_aleatorio [escolhe-1])
                        
                        movimentos_possiveis = lista_movimentos_possiveis(baralho_aleatorio, escolhe-1)
                        if movimentos_possiveis == []:
                            print (bcolors.FAIL +'Não há movimentos possíveis para a carta {0}, escolha outra!'.format (baralho_aleatorio [escolhe-1]) + bcolors.RESET)
                            

                        if movimentos_possiveis == [1]:
                            baralho_aleatorio = empilha (baralho_aleatorio, escolhe-1, escolhe-2)
                            f = False
                        if movimentos_possiveis == [3]:
                            baralho_aleatorio = empilha (baralho_aleatorio, escolhe-1, escolhe-4)
                            f = False
                        if movimentos_possiveis == [1,3]:
                            t = True
                            while t:
                                decide = input('Escolha empilhar a carta {0} sobre: 1. {1} ou 2. {2}: '. format (colore_baralho(baralho_aleatorio[escolhe - 1]), colore_baralho(baralho_aleatorio [escolhe - 2]), colore_baralho(baralho_aleatorio [escolhe - 4])))
                                if not decide.isdigit():
                                    print("Digite apenas 1 ou 2!")
                                if decide.isdigit():
                                    decide = int (decide)
                                    if decide != 1 and decide != 2:
                                        print (bcolors.FAIL + 'Escolha um número entre 1 e 2!'.format(len(baralho_aleatorio))+ bcolors.RESET)
                                    if decide == 1:
                                        baralho_aleatorio = empilha(baralho_aleatorio, escolhe-1, escolhe-2)
                                        f = False
                                        t = False
                                    if decide == 2:
                                        baralho_aleatorio = empilha(baralho_aleatorio, escolhe-1, escolhe-4)
                                        f = False
                                        t = False
                    
        elif possui_movimentos_possiveis(baralho_aleatorio) == False:
            if len (baralho_aleatorio) > 1:
                print ('Não há mais movimentos possíveis no baralho, você perdeu!')
                denovo = input ('Digite "sim" se deseja jogar novamente: ')
                if denovo != 'sim':
                    p = False
                if denovo == 'sim':
                    p = True
                    baralho_aleatorio = []
                    baralho = cria_baralho ()
                    for k in range(len(cria_baralho())):
                        tira_esse = random.choice (baralho)
                        baralho_aleatorio.append (tira_esse)
                        baralho.remove (tira_esse)
                
            if len(baralho_aleatorio) == 1:
                print ('Você venceu!')
                denovo2 = input ('Digite "sim" se deseja jogar novamente: ')
                if denovo2 != 'sim':
                    p = False
                if denovo2 == 'sim':
                    p = True
                    baralho_aleatorio = []
                    baralho = cria_baralho ()
                    for k in range(len(cria_baralho())):
                        tira_esse = random.choice (baralho)
                        baralho_aleatorio.append (tira_esse)
                        baralho.remove (tira_esse)
                
            