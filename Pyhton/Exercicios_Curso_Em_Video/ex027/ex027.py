nome = str(input("digite o seu nome completo para analisarmos: ")).strip()
nome = nome.split()

print("""O seu primeiro nome é: {}
O seu ultimo nome é: {}""".format(nome[0], nome[-1]))  # nome[len(nome)] -1
# apenas botar o -1 no index de uma lista, mostra o primeiro item da direta para
# a esquerda
