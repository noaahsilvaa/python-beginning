import math
n = float(input('Digite um número real: '))
nn = math.trunc(n)
print('O valor inteiro de {} é equivalente a {}'.format(n, nn))
'''outras resoluções válidas:
import math
n = float(input('Digite um número real: '))
print('O valor inteiro de {} é equivalente a {}'.format(n, math.trunc(n)))

ou também:
from math import trunc
n = float(input('Digite um número real: '))
print('O valor inteiro de {} é equivalente a {}'.format(n, trunc(n)))

sem usar módulo também:
n = float(input('Digite um numero real:))
print('O valor inteiro de {} é equivalente a {}'.format(n, int(n)))'''
