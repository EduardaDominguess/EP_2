from funcoes import *
from criaPeças import *
from inicia_jogo import *
from Possível_mão import *
from Soma_de_peças import *
#from verifica_ganhador import *


print()
print('Jogo de Dominó')
print()

numero_jogadores = num_jogadores
peças = cria_pecas()
inicio = inicia_jogo(numero_jogadores, peças)

quem_comeca = random.randint(0,num_jogadores -1)

winner = -1
som_peças = 0

while winner == -1 and som_peças <num_jogadores:
    mesa = inicio ['mesa']
    peças = inicio ['jogadores'][quem_comeca]
    possivel = posicoes_possiveis[mesa, peças]

    

