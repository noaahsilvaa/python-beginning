preco = float(input('PREÇO DO PRODUTO: R$'))
percentual = float(input('PERCENTUAL A SER APLICADO: '))
desconto = (preco*percentual/100)
pfinal = preco - desconto
print('O valor do desconto é de R${}'.format(desconto))
print('O valor final do produto é de R${}'.format(pfinal))