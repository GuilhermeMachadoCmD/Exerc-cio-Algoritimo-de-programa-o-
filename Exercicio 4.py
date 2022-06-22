n1 = []
qd = []
mp = 0

for x in range(10):
    n1.append(int(input("Digite um número inteiro: ")))
for i in n1:
    mp = mp + n1[x] ** 2
    qd.append(mp)

print('Os números da lista é: ', n1)
print('A soma dos número elevados ao quadrado é: ', mp)