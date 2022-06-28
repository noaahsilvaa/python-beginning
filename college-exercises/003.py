km = float(input('QUANTIDADE DE KM PERCORRIDO: '))
dias = float(input('POR QUANTOS DIAS O CARRO FOI ALUGADO? '))
aluguel = dias*60 + km*0.15
print('O valor total do aluguel do carro é de R${}'.format(aluguel))