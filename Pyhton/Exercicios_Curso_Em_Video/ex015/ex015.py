########################################################
"""
dias = int(input('Quantos dias alugados? ))
km = float(input('Quantos Km rodados? ))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
"""
########################################################
dias = int(input('Quantos dias voce alugou o carro? '))
km = float(input('Quantos Km voce pecorreu? '))
valor_dias = 60 * dias
valor_km = 0.15 * km
valor_pg = valor_dias + valor_km

print('Voce deve pagar R${:.2f} pelo carro alugado_ Obrigado pela preferência_'
      .format(valor_pg).replace('.',',').replace('_','.'))
