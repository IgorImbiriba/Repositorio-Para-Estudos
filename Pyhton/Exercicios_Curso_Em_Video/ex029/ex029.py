# O mesmo programa que o do professor
veloc = int(input('A que velocidade voce esta andando? '))

if veloc > 80:
    multa = (veloc - 80) * 7
    print('Você foi multado por estar andando a {}Km/h, e deve pagar R${:.2f}'
          .format(veloc, multa).replace('.',','))
else:
    print('Parabens você está seguindo as leis de trânsito')
