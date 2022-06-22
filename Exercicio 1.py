medAlunos = []
alunosMedia = 0

for aluno in range(3):
    somaNotas = 0

    print(aluno + 1, 'º aluno')
    for nota in range(4):
        somaNotas += float(input("Digite a nota do aluno: "))

    medAlunos.append(somaNotas / 4)

    if medAlunos[aluno] >= 7:
        alunosMedia += 1

print('O número de alunos acima da média é de: ', alunosMedia)