import random
from time import sleep
n = random.randint(0, 5) # faz o computador "pensar"
print('-=-'*20)
print('O computador irá sortear um número de 0 a 5.')
print('Tente descobrir qual é!')
print('-=-'*20)
adv = int(input('DIGITE UM NÚMERO: ')) # jogador tenta advinhar
print('PROCESSANDO...')
sleep(3) #vai fazer o computador "dormir" por (x) segundos. vai criar uma espera
if adv == n:
    print('PARABÉNS, VOCÊ ACERTOU :)')
    print('O NÚMERO SORTEADO FOI {}'.format(n))
else:
    print('VOCÊ ERROU!!! :p')
    print('O NÚMERO SORTEADO FOI {}'.format(n))
