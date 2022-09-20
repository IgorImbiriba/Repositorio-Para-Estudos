preco = float(input('Qual o preço do produto? R$ '))
desconto = float(input('Quantos % de desconto? '))
novoPreco = preco - (preco * (desconto / 100))

print('O produto no valor de R$',f'{preco:.2f}'.replace('.',','),
      f'\nrecebeu um desconto de {desconto}%.'      
      '\nvoce vai pagar R$',f'{novoPreco:.2f}'.replace('.',','))
