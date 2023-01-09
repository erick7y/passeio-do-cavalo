'''
 8 | | | | | | | | |
 7 | | | | | | | | |
 6 | | | | | | | | |
 5 | | | | | | | | |
 4 | | | | | | | | |
 3 | | | | | | | | |
 2 | | | | | | | | |
 1 | | | | | | | | |
    a b c d e f g h
'''

from random import choice
from random import randint
from notation import from_collection_to_chess_notation

'''
`old_pos` deve ser uma posição válida no tabuleiro de Xadrez padrão (tabuleiro
de 64 casas.). Essa função nunca retorna uma posição que não esteja no tabuleiro
padrão de Xadrez de 64 casas.
'''
def mov_horse(old_pos):
  pos = []

  while True:
    if choice([0, 1]) == 0:
      pos.append(old_pos[0] + choice([2, -2]))
      pos.append(old_pos[1] + choice([1, -1]))
    else:
      pos.append(old_pos[0] + choice([1, -1]))
      pos.append(old_pos[1] + choice([2, -2]))

    if pos[0] > 8 or pos[0] < 1 or \
       pos[1] > 8 or pos[1] < 1:
      pos = []
      continue

    break

  return pos

if __name__ == '__main__':
  print('Resolvendo...')
  while True:
    positions = [mov_horse([randint(1, 8), randint(1, 8)])]

    while len(positions) < 64:
      positions.append(mov_horse(positions[-1]))

    # verifica se o problema do passeio do cavalo foi resolvido.
    solved = True
    for position in positions:
      if positions.count(position) > 1:
        positions = []
        solved = False
        break

    if not solved:
      continue

    print(positions)
    break
