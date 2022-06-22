matriz=[[0,0,0],[0,0,0],[0,0,0]]
for x in range(3):
    for y in range(3):
        matriz[x][y]=int(input('Digite o elemento:  [' + str(x) + ']['+ str(y) +']: '))
print('\n')
v=int(input('Digite um número para multiplicar os elementos da diagonal principal: '))
for i in range(3):
    for j in range(3):
        if x==y:
            matriz[x][y]=x*matriz[x][y]
print(matriz)