nome = input("Digiteseu nome: ")
print(*input("confirme seu nome: "), sep="\n")
x = len(nome)+1
for l in range(x):
    print(nome[:l])