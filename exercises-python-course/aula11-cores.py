a = 3
b = 5
#print('Os valores são \033[32m{}\033[m e \033[36m{}\033[m'.format(a, b))

#ou

nome = 'Noah'
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m'} #usando dicionário
print('Prazer em te conhecer, {}{}{}!!'.format(cores['amarelo'], nome, cores['limpa']))
#print('Prazer em te conhecer, {}{}{}!!'.format('\033[1;31m', nome, '\033[m'))