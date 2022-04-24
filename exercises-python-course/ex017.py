from math import pow, sqrt, trunc
cato = float(input('DIGITE A MEDIDA DO CATETO OPOSTO: '))
catadj = float(input('DIGITE A MEDIDA DO CATETO ADJACENTE: '))
h = trunc(sqrt(pow(cato, 2) + pow(catadj, 2)))
print('UM TRIANGULO RETÂNGULO DE CATETO OPOSTO {} E CATETO ADJASCENTE {} TEM HIPOTENUSA MEDINDO {}'.format(cato, catadj, h))
