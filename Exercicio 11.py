matriz=[[0,0,0],[0,0,0],[0,0,0]]
for x in range(3):
    for j in range(3):
        matriz[x][j]=int(input('Digite o elemento:  [' + str(x) + ']['+ str(y) +']: '))
print('\n')
a= int(input('Digite um número para multiplicar os numeros da diagonal: '))
for x in range(3):
    for y in range(3):
        if x==y:
            matriz[x][y]=v*matriz[x][y]
print(matriz)