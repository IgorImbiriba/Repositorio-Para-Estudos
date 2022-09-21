from random import choice
# Função choice() para escolher um indice da lista turma
a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º alumo: ')
turma = [a1, a2, a3, a4] # criado uma lista chamada de 'turma'
# escolhido = choice(turma) # o professor ja faz a escolha fora do print
print('O aluno escolhido foi: {}'.format(choice(turma))) # Eu fiz a escolha 
                                                         # dentro do print
                                                         