nome = input('Qual o funcionario? ')
salario = float(input('Qual o salario do {}? R$'.format(nome)))
acrecimo = float(input('Quantos % o {} ganhou de extra? '.format(nome)))
novoSal = salario + (salario * ( acrecimo / 100))

print(f'O {nome}, que tinha um salario de R${salario:.2f}'
      f'\nTeve um bom rendimento e por isso teve {acrecimo}% acescentados em seu salario'
      f'\nSeu novo salario é de R${novoSal:.2f}'.replace('.',','))