import numpy as np
from criaPeças import *
from inicia_jogo import *
from Possível_mão import *
from Soma_de_peças import *
from verifica_ganhador import *
from AdicionaMesa import *
from random import *

print()
print('Jogo de Dominó')
print()


players = 0
while players < 2 or players > 4:
  players = int(input('Informe o número de Jogadores (2-4): '))
  if players < 2 or players > 4:
    print('Resposta inválida')


peças = cria_pecas
inicio = inicia_jogo
mesa = inicio ['mesa']
pecas_jogadores = inicio['jogadores']
monte = inicio['monte']

ordem_jogadores = np.arange(0, players)
random.shuffle(ordem_jogadores)

print(f'Temos {players} com 7 peças cada. \n')

jogo = True
while jogo == True: 
    for i in ordem_jogadores:
            print(f'Tamanho monte {len(pecas_jogadores)} peças.')
            print(f'Mesa: {mesa}')
            print('')

            if i != 0:
                print(f'Peças jogador {i}: {len(pecas_jogadores[i])} ')
            else:
                print(f'Peças jogador {0}: {len(pecas_jogadores[0])} ')
                print(pecas_jogadores[0])
            
            print('')

            if len(posicoes_possiveis(mesa,pecas_jogadores[i])) >= 1  and i == 0 :
                print(posicoes_possiveis(mesa, peças_jogadores[i])
           

            if i == 0:
                começa_a_jogar = int(input('Escolha uma peça para jogar: '))
                mesa_add(pecas_jogadores[i][começa_a_jogar], mesa)
                pecas_jogadores[i].pop(jogar)

#Comprar do monte

            comprar_do_monte = 0
            while len(posicoes_possiveis(mesa, pecas_jogadores[0])) == 0 and len(pecas_jogadores[0]) > 0:
                entrada = input('Não tem peças possíveis. PEGANDO DO MONTE! [pressione ENTER]')
            
                if entrada == '':
                    pecas_jogadores[0].append(monte(0))
                    monte.pop(0)
                    compra_do_monte += 1

                else: 
                    print('Opção inválida [pressione ENTER]' )

                      

