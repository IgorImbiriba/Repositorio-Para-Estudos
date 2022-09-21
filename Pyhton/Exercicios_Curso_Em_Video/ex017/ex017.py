from math import hypot 
print('Vamos calcular o valor da hypotenusa de um triangulo retêngulo?')
catAdj = float(input('Digite o valor do cateto adjacente: '))
catOpo = float(input('digite o valor do cateto oposto: '))
#fromula da hipotenusa hi = (x**2 + y**2)**(1/2)
hipo = hypot(catAdj,catOpo) # calcula o valor da hipotenusa
print('A hipotenusa do triangulo retêngulo é: {:.2f}'.format(hipo))
