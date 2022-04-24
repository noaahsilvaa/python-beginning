print('-----'*5)
print('JULGADOR DE NOMES')
print('-----'*5)
nome = str(input('Qual é o seu nome?')).strip().capitalize()
cores = {'limpa': '\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'verde': '\033[32m',
         'vermelho':'\033[31m',
         'roxo':'\033[35m'}
if nome == 'Noah':
    print('Que nome lindo {}{}{} {}(✿ ♡‿♡){}'.format(cores['azul'],nome,cores['limpa'],cores['vermelho'],cores['limpa']))
elif nome in "Nate Gabriel Leite":
    print('Acho que você tem uma namorada muito linda {}{}{} {}♥{}╣[-_-]╠{}♥{}'.format(cores['roxo'], nome,cores['limpa'],cores['vermelho'],cores['limpa'],cores['vermelho'],cores['limpa']))
elif nome in 'Leandro Lizandro Hittler Bolsonaro Jair Adolf Amarante':
    print('VAI TOMAR NO SEU CU╭∩╮ಠ_ಠ╭∩╮')
elif nome in 'Ana Maria CLáudia Pedro Paulo Miguel Lucy Débora Kaylane':
    print('Que nome popular amg :/')
else:
    print('Você tem um nome muito normal¯\_(ツ)_/¯')
