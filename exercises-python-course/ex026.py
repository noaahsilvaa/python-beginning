frase = str(input('Digite uma frase: ')).strip().upper()
print('QUANTAS VEZES APARECE A LETRA "A" na frase: {}'.format(frase.count('A')))
print('A POSIÇÃO EM QUE ELA APARECE PELA PRIMEIRA VEZ: {}'.format(frase.find('A')+1))
print('A POSIÇÃO EM QUE ELA APARECE PELA ÚLTIMA VEZ: {}'.format(frase.rfind('A')+1))