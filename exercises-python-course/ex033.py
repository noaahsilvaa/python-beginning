x = int(input('DIGITE UM NÚMERO: ' ))
y = int(input('DIGITE OUTRO NÚMERO: '))
z = int(input('DIGITE MAIS UM NÚMERO: '))
# verificando quem é o menor
if x<y and x<z:
    menor = x
else:
    if y<x and y<z:
        menor = y
    else:
        if z<x and z<y:
            menor = z
if x>y and x>z: # verificando quem é o maior
    maior = x
else:
    if y>x and y>z:
        maior = y
    else:
        if z>x and z>y:
            maior = z
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))
