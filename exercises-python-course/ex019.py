from random import choice
a1 = str(input('aluno 1: '))
a2 = str(input('aluno 2: '))
a3 = str(input('aluno 3: '))
a4 = str(input('aluno 4: '))
lista = [a1, a2, a3, a4]
escolhido = choice(lista)
print('O ALUNO ESCOLHIDO FOI {}'.format(escolhido))
