num = int(input('DIGITE UM NÚMERO INTEIRO: '))
print('''PARA QUAL BASE VOCÊ DESEJA CONVERTER?
[1] binário
[2] octal
[3] hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido pra base binária é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para base octal é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para base hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inbválida. Tente novamente :(')