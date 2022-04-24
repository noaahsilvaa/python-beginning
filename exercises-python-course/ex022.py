nome = str(input('DIGITE SEU NOME COMPLETO: ')).strip()
print('EM LETRAS MAIÚSCULAS: {}'.format(nome.upper()))
print('EM LETRAS MINÚSCULAS: {}'.format(nome.lower()))
nome2 = nome.split()
print('QUANTAS LETRAS SEM CONTAR ESPAÇOS: {}'.format(len(''.join(nome2))))
print('SEU PRIMEIRO NOME É {} E ELE POSSUI {} LETRAS'.format(nome2[0], len(nome2[0])))
#caralho quebrei a cabeça nesse aqui meu deus do céu mas deu muito certo eu não to nem acreditandoooo.