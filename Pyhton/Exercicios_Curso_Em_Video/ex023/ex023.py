num = int(input('digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o Numero Digitado:')
print('unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('centena: {}'.format(c))
print('milhar: {}'.format(m))
