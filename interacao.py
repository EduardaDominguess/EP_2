from criaPeças import *
from inicia_jogo import *
from Possível_mão import *
from Soma_de_peças import *
from verifica_ganhador import *
from AdicionaMesa import *


print()
print('Jogo de Dominó')
print()


def num_jogadores():
  players = 0
  while players < 2 or players > 4:
    players = int(input('Informe o número de Jogadores (2-4): '))
    if players < 2 or players > 4:
      print('Resposta inválida')
  return players


peças = cria_pecas
inicio = inicia_jogo
mesa = inicio ['mesa']




