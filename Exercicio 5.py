xVetor = []
yVetor = []
zVetor = []

for p in range(10):
    xVetor.append(input("Digite o elemento da " + str(p + 1) + "ª posição do primeiro vetor: "))
print('-__-'*32)
for a in range(10):
    yVetor.append(input("Digite o elemento da " + str(q + 1) + "ª posição do segundo vetor: "))
print('-__-'*32)
for l in range(10):
    zVetor.append(xVetor[l])
    zVetor.append(yVetor[l])
print('-__-'*32)
print(xVetor)