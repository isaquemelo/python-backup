qnt = int(input())
count = 0
linhas = []
while count < qnt:
    count += 1
    linha = input().split()
    linhas.append(linha)

for i in range(len(linhas)):
    for f in range(len(linhas[i])):
        linhas[i][f] = int(linhas[i][f])


somas = []
somas2 = []
colunas = []
colunas_formatas = []

for f in range(len(linhas)):
    for i in range(len(linhas)):
        colunas.append(linhas[i][f])

for g in range(0,len(colunas),qnt):
    colunas_formatas.append(colunas[g:g+qnt])

for i in range(len(linhas)):
    somas.append(sum(linhas[i]))

for i in range(len(colunas_formatas)):
    somas2.append(sum(colunas_formatas[i]))

diagonal1 = []

for i in range(len(linhas)):
    diagonal1.append(int(linhas[i][i]))

count2 = 0
diagonal2 = []

for f in range(len(linhas)-1,-1,-1):
    diagonal2.append(linhas[count2][f])
    count2 += 1
elementos = [diagonal1, diagonal2]

somas3 = []
for i in range(len(elementos)):
    somas3.append(sum(elementos[i]))

if all(x==somas[0] for x in somas) and all(x==somas2[0] for x in somas2) and all(x==somas3[0] for x in somas3):
    print(somas[0])
else:
    print("-1")