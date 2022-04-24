val = float(input('Qual o valor do produto? R$'))
newval = val - (5 / 100 * val)
print('O novo valor do produto que antes custava {}, com 5% de desconto é igual a {}'.format(val, newval))