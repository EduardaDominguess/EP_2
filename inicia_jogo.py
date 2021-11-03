def inicia_jogo(n, pecas):

    distribuidas = {}
    distribuidas['jogadores'] = {}

    for i in range(n):
        distribuidas['jogadores'][i]= pecas[0:7]
        del pecas[0:7]

    distribuidas['monte'] = pecas
    distribuidas['mesa']= []
    
    return distribuidas
