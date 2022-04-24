from datetime import date #esse módulo vai oegar o ano atual da máquina
ano = int(input('QUE ANO QUER ANALISAR? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year # vai pegar o ano atual configurado na máquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print('O ANO {} É BISSEXTO'.format(ano))
else:
    print('O ANO {} NÃO É BISSEXTO'.format(ano))