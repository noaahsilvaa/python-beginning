#condições pra existência de um triângulo:
'''A medida de cada lado de um triângulo deve ser menor que a soma e maior que o módulo (número sem sinal) da diferença
dos outros dois'''
'''Assim sendo: pra um triângulo existir é necessário apenas:
|b - c| < a < b + c
|a - c| < b < a + c
|a - b| < c < a + b'''
lado1 = float(input('LADO 1: '))
lado2 = float(input('LADO 2: '))
lado3 = float(input('LADO 3: '))
if lado1 < lado2 + lado3 and lado1 > abs(lado2 - lado3) and lado2 < lado1 + lado3 and lado2 > abs(lado1 - lado3) and lado3 < lado1 + lado2 and lado3 > abs(lado1 - lado2):
    print('OS VALORES PODEM FORMAR UM TRIÂNGULO!')
    if (lado1 == lado2 or lado1 == lado3) and lado3 != lado2:
        print('E ESSE TRIÂNGULO É ISÓSCELES.')
    else:
        if lado1==lado2 and lado1==lado3 and lado3==lado2:
            print('E ESSE TRIÂNGULO É EQUILÁTERO.')
        else:
            if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
                print('E ESSE TRIÂNGULO É ESCALENO!')
else:
    print('OS VALORES NÃO PODEM FORMAR UM TRIÂNGULO!')