cid = str(input('Digite o nome completo de uma cidade: ')).strip()
cid = cid.split() # criei uma lista com os nomes separados
# print(cid[:5].upper() == 'SANTO') 
# aqui o prfessor utilizou a tecnica de fatiamento de string 
print("A didade começa com Santo? ",'santo' in cid[0].lower())
print("A didade começa com Santo? ",cid[0].lower() == 'santo')
# chamei o primeiro indice da lista e verifiquei se é santo com o in e com o ==
