
print('voce quer pintar uma parede? ')
altPar = float(input('Me diga, em metros, a altura da parede: '))
larPar = float(input('Me diga, em metro, a largura da parede: '))

area = altPar * larPar

litTint = area/2

print('A sua parede tem {}m², você vai precisar de {}L de tinta para \n'
      'pintar toda a parede'.format(area, litTint))

