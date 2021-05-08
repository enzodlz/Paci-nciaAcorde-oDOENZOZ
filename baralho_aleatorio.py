import random
def cria_baralho ():
    
    paus = ['A♣','2♣','3♣','4♣','5♣','6♣','7♣','8♣','9♣','10♣','Q♣','J♣','K♣']
    copas = ['A♥','2♥','3♥','4♥','5♥','6♥','7♥','8♥','9♥','10♥','Q♥','J♥','K♥']
    espadas = ['A♠','2♠','3♠','4♠','5♠','6♠','7♠','8♠','9♠','10♠','Q♠','J♠','K♠']
    ouros = ['A♦','2♦','3♦','4♦','5♦','6♦','7♦','8♦','9♦','10♦','Q♦','J♦','K♦']
    lista_de_cartas = paus + copas + espadas + ouros
    return lista_de_cartas
print (random.choice (cria_baralho()))

baralho_aleatorio = []
baralho = cria_baralho ()
for k in range(len(cria_baralho())):
    tira_esse = random.choice (baralho)
    baralho_aleatorio.append (tira_esse)
    baralho.remove (tira_esse)

print (len(baralho_aleatorio))
print (len(cria_baralho()))
print (baralho_aleatorio)
