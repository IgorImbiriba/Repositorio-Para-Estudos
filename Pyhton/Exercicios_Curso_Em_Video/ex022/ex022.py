nome = input('Digite seu nome para analisarmos ele: ').strip()
#soEsp = nome.strip().count(' ')
#socarac = len(nome) - soEsp
nomeSep = nome.split()
print('''O seu nome com todas as letras maiusculas fica assim {}
O seu nome com todas a letras minusculas fica assim {}
O seu nome tem um total de {} letras
O seu primeiro nome {} tem {} letras
'''.format(nome.upper(), nome.lower(), len(nome) - nome.count(' '),
           nomeSep[0], len(nomeSep[0])))
#print(nome.find(' ')) # iria retornar o valor 5 pois o 1º 'espaço' 
#esta no index 5 da string
