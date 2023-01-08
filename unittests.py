'''
Testes unitários para o módulo chess.py.
'''

from chess import mov_horse

def test_mov_horse():
  result = mov_horse([5, 4])

  if result not in [[4, 2], [6, 2], [4, 6], [6, 6], [3, 3], [3, 5], [7, 3], [7, 5]]: # d2, f2, d6, f6, c3, c5, g3, g5
    print('Teste não passado.')
    return False

  print('Teste passado.')

  '''
  outro teste.
  '''
  result = mov_horse([1, 1])

  if result not in [[3, 2], [2, 3]]: # c2, b3
    print('Teste não passado.')
    return False

  print('Teste passado.')

  return True

if __name__ == '__main__':
  test_mov_horse()
