d = float(input('DISTÂNCIA PERCORRIDA EM KM: '))
# preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
if d <= 200:
    passagem = d*0.50
else:
    passagem = d*0.45
print('O VALOR DA PASSAGEM É IGUAL A R${}'.format(passagem))