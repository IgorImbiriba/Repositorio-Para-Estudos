##############################################################
"""
n = int(input('Digite um valor: ')) 
d = n * 2
t = n * 3
rq = n ** (1/2)
print('O dobro de {} vale {}'.format(n, d))
print('O tripo de {} vale {}. \nA raiz quadrada de {} vale {:.2f}
       ' '.format(n, t, n, r))
"""
################################################################

valor = int(input('Digite um valor: '))
print('O valor é {}, seu dobro é {}, seu triplo é {}, a raiz quadrada é {}'
      .format(valor, valor*2, valor*3, valor**(1/2)))