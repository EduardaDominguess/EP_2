def soma_pecas(pecas):
    soma_pecas = 0
    for i in range(len(pecas)):
        soma_pecas += (pecas[i][0] + pecas[i][1])
    return soma_pecas
