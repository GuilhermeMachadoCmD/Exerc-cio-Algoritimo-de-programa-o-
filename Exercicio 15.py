def funcao1(a):
    if a > 0:
        print('Positivo')
    elif a == 0:
        print('Nulo')
    else:
        print('Negativo')

print('Positivo ou negativo ')
a = int(input('digite um número: '))
print('Este número é', end=' ')
funcao1(a)