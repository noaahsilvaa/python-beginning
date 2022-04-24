v = float(input('Qual a velocidade do carro? '))
if v > 80:
    print('Você foi multado!')
    multa = (v - 80)*7
    print('Valor da multa R${}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')
