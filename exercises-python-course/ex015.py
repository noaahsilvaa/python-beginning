dia = float(input('DIAs DE ALUGUEL DO CARRO: '))
km = float(input('KM RODADOS:'))
price = 60 * dia + km * 0.15
print('O VALOR FINAL DO ALUGUEL DO CARRO É R${:.2f}'.format(price))