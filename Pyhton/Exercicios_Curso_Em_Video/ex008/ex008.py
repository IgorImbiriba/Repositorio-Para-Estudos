metro = float(input('digite um valor em metro: '))
kilom = metro /1000
hectom = metro / 100
decam = metro / 10
decim = metro * 10 
cent = metro * 100
mili = metro * 1000

print('''{} metro, igual à
{} kilometro
{} hectometros
{} decametros
{} decimetro
{} centimetros
{} milimetros.'''.format(metro, kilom, hectom, decam, decim, cent, mili))