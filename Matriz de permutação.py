qnt = int(input())
matriz = list(input().replace(" ", ""))
count = 0

linhas = []
colunas = []
colunas_formatas = []
n = qnt
#print(matriz)

for i in range(0,len(matriz),n):
    linhas.append(matriz[i:i+n])
    #print(matriz[i:i+n])

for f in range(len(linhas)):
    for i in range(len(linhas)):
        colunas.append(linhas[i][f])

for g in range(0,len(colunas),qnt):
    colunas_formatas.append(colunas[g:g+qnt])

#print(linhas)
#print(colunas_formatas)


def verifica(linhas):
    nulo = 0
    uns = 0
    count = 0
    for f in range(len(linhas)):
        for i in range(len(linhas[f])):
            if linhas[f][i] == '0':
                nulo += 1
                
            elif linhas[f][i] == '1':
                uns += 1

            if (nulo == len(linhas) - 1) and uns == 1:
                count += 1

        nulo = 0
        uns = 0
    if count == len(linhas):
        return True
    else:
        return False


if verifica(linhas) and verifica(colunas_formatas):
    for i in linhas:
        for f in i:
            print(f,end=" ")
        print()

    print("True")
else:
    for i in linhas:
        for f in i:
            print(f,end=" ")
        print()

    print("False")
#print(linhas)

