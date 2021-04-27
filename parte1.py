def cria_baralho ():
    
    paus = ['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','Q♣','J♣','K♣']
    copas = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','Q♥','J♥','K♥']
    espadas = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','Q♠','J♠','K♠']
    ouros = ['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','Q♦','J♦','K♦']
    lista_de_cartas = paus + copas + espadas + ouros
    return lista_de_cartas
print (cria_baralho())