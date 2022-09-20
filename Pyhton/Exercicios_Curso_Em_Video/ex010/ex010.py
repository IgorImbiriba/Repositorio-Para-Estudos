real = input('quanto dinheiro voce tem? ')
dolar = float(real)/3.27
real = f'{float(real):.2f}'.replace('.',',')

print('Você tem R${} e pode comprar ${:.2f} dolares'.format(real, 
    dolar))