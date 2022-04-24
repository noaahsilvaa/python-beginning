import math
ang = float(input('VALOR DO ÂNGULO: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O ÂNGULO DE {} TEM SENO {:.2f}, COSSENO {:.2f} E TAGENTE {:.2f}'.format(math.trunc(ang), sen, cos, tan))
