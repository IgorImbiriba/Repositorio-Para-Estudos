dado = input('digite algo: ')

print('O tipo primitivo desse dado é {}'.format(type(dado)))
print('O que voce digitou so tem espaços? {}'.format(dado.isspace()))
print('O que voce digitou é um numero? {}'.format(dado.isnumeric()))
print('O que voce digitou é alfabetico? {}'.format(dado.isalpha()))
print('O que voce digitou é alfanumerico? {}'.format(dado.isalnum()))
print('O que voce digitou esta tudo em MAIUSCULO? {}'.format(dado.isupper()))
print('O que voce digitou esta tudo em minusculo? {}'.format(dado.islower()))
print('O que voce digitou tem a primeira letra maiuscula? {}'
      .format(dado.istitle()))
print('O que voce digitou começa com uma Letra, tem numero ou "_" depois? {}'
      .format(dado.isidentifier()))
print('O que voce digitou, tem na tabela ASCII? {}'.format(dado.isascii()))
print('O que voce digitou é um decimal(0 a 9)? {}'.format(dado.isdecimal()))
print('O que voce digitou é um digito? {}'.format(dado.isdigit()))
print(dado.isprintable())
