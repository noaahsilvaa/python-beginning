city = str(input('DIGITE O NOME DA CIDADE: ')).strip()
city2 = city.split()
print('A cidade {} começa com a palavra "Santo" ? {}'.format(city, city2[0].upper() == 'SANTO'))
#nesse caso o operador == funciona melhor que o Santo in