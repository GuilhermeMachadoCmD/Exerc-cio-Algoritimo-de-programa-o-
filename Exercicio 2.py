vet = []
mult = 1
soma = 0

for x in range(5):
    vet.append(int(input('Insira os numeros: ')))

for v in vet:
    soma += v
    mult *= v

print('A soma dos números é: ', soma)
print('A multiplicação dos números é: ', mult)
print(vet)
