def posicoes_possiveis (mesa , pecas):
    Posicoes_possíveis = []
    
    if (len(mesa)) == 0:
        i= 0 
        while i < len(pecas):
            Posicoes_possíveis.append(i)
            i += 1
            #return Posicoes_possíveis
    else:
        p1=mesa[0][0]
        p2=mesa[-1][1]
        ii = 0
        while ii < len(pecas):
            if pecas[ii][0] == p1 or pecas[ii][1] == p1 or pecas[ii][0] == p2 or pecas[ii][1] == p2 :
                Posicoes_possíveis.append(ii)
            ii += 1
    return Posicoes_possíveis
