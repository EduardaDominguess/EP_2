def adiciona_na_mesa (peca, mesa):
    peca_invertida = peca[::-1]
    if (len(mesa)) == 0:
        mesa.append(peca)
    elif peca[0] == mesa[0][0]:
        mesa.insert(0, peca_invertida) 
    elif peca[1] == mesa[0][0]:
        mesa.insert(0, peca)
    elif peca[0] == mesa[-1][1]:
        mesa.append(peca) 
    elif peca[1] == mesa[-1][1]:
        mesa.append(peca_invertida) 
    else:
        mesa = mesa
    return mesa
