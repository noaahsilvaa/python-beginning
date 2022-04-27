val= float(input('Qual o valor da casa? R$'))
sal= float(input('Qual o salário do comprador? R$'))
anos= float(input('Em quantos anos vai ser pago? '))
prest= val/(anos*12)
sal30= (30/100*sal)
if prest > sal30:
    print('A PRESTAÇÃO CALCULADA EXCEDE 30% DO SEU SALÁRIO!')
    print('EMPRÉSTIMO NEGADO!')
else:
    print('DE ACORDO COM SEU SALÁRIO, VOCÊ PODE PAGAR')
    print('EMPRÉSTIMO APROVADO!')
