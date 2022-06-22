def somadosimpostos(taxaImposto, Custo):
    return (1 + taxaImposto/100)*Custo
x = float(input('Digite a taxa de imposto: '))
y = float(input('Digite o custo: '))
print('Valor com imposto:', somadosimpostos(x, y))