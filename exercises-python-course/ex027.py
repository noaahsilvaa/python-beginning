name = str(input('Digite seu nome completo: ')).strip()
name2 = name.split()
print('primeiro nome: {}'.format(name2[0]))
print('último nome: {}'.format(name2[-1]))
#o valor entre colchetes é a posição do item que vc quer acessar na lista.
#lista[0], se refere ao primeiro item da lista, lista[1] ao segundo e assim por diante.
# Se vc utilizar valores negativos dentro do colchete, vc acessa valores a partir do final da lista, em direção ao inicio,
# ou seja: lista[-1] se refere ao último item da lista, lista[-2] ao penúltimo, etc..