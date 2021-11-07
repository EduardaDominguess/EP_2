def num_jogdores():
  players = 0
  while players < 2 or players > 4:
    players = int(input('Informe o número de Jogadores (2-4): '))
    if players < 2 or players > 4:
      print('Resposta inválida')
  return players
    
                  
    
    
  
