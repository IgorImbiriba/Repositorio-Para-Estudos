# o mesmo programa que o do professor
from random import randint

print('Tente adivinhar o numero que o PC escolheu')
usu = int(input('digite um numero de 0 a 5: '))
pc = randint (0, 5)

if usu == pc:
  print('Voce venceu, Parabens')
else:
  print('O pc escolheu {}, e voce escolheu {}'.format(pc, usu))
  print('Game Over, tente novamente')