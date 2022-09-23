###################################################
#             Metodo if tradicional
"""
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viajem de {} km'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('E o preço da sua viajem será de R${:.2f}'.format(preco))
"""
###################################################
#               Metodo if simplificado
"""
distancia = float(input('Qual é a distancia da sua viagem? '))
print('Você está prestes a começar uma viajem de {} km'.format(distancia))
preco = distancia * 0.50 if distancia <=200 else distancia * 0.45
print('E o preço da sua viajem será de R${:.2f}'.format(preco))
"""
####################################################
print('Vamos calcular o preço da sua passagem')
dist = float(input('Qual a distancia, em km, da sua viagem? '))

if dist <= 200:
    val = 0.50 * dist
    print('Voce vai viajar por {:.2f} KM, a passagem vai custar R${:.2f}'
          .format(dist, val))
else:
    val = 0.45 * dist
    print('Voce vai viajar por {:.2f} km, a passagem vai custar R${:.2f}'
          .format(dist, val))