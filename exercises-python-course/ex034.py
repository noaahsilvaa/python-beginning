from time import sleep
print('-'*30)
print('CÁLCULO DE AUMENTO SALARIAL')
print('-'*30)
sal = float(input('SALÁRIO ATUAL: R$'))
if sal >= 1250:
    aumento = sal + (sal * 10 / 100)
else:
    aumento = sal + (sal * 15 / 100)
print('calculando...')
sleep(2)
print('NOVO SALÁRIO COM AUMENTO: R${}'.format(aumento))