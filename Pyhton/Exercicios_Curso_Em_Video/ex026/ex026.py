txt = str(input('digite uma frase qualquer: ')).strip()
print("""Na frase digitada tem {} letras 'a' e {} letras 'A'
O 1° a/A aparece na {}ª posição
O ultimo a/A aparece na {}ª posição""".format(txt.count('a'), txt.count('A'),
                                              txt.lower().find('a') + 1,
                                              txt.lower().rfind('a')+1))
