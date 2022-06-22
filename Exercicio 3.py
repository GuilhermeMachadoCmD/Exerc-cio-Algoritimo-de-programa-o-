idade = []
altura = []
x = 0

for y in range(5):
    print(x+1, '° Pessoa')
    altura.append(float(input("Qual é a altura da pessoa? ")))
    idade.append(int(input('Qual é a idade da pessoa? ')))

print('idade normal', idade)
print('idade invertida', (idade[::-1]))
print('altura normal', altura)
print('altura invertida', (altura[::-1]))
