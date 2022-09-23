from datetime import date
ano = int(input('Digite um ano: '))
if ano == 0:
    ano = int(date.today().year)
print('O ano de {}'.format(ano), end =' ' )
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('é ano bissesto')
else:
    print('não é ano bissesto') 