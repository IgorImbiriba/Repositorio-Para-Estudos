from math import cos, sin, tan, radians
print('Vamos calcular os valores de Seno, Cosseno e Tagente?')
angulo = float(input('digite um angulo para calcular o seno, '
                      'cosseno e a tangente: '))
# É preciso encontrar os valores em radianos do angulo especificado
# Para isso isso utiliza-se a função radians() do modulo math
seno = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))

print("""para o angulo de {:.1f}°
O valor do seno é {:.2f}.
O valor do cosseno é {:.2f}.
O valor da tangete é {:.2f}.""".format(angulo, seno, coss, tang))
