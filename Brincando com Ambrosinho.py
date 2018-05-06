'''
1 2 3
4 5 6
7 8 9

LINHA, COLUNA -> LINHA, COLUNA

0,0 -> 0,2
0,1 -> 1,2
0,2 -> 2,2

1,0 -> 0,1
1,1 -> 1,1
1,2 -> 2,1

2,0 -> 0,0
2,1 -> 1,0
2,2 -> 2,0



Padrão colunas:
    De len(colunas) até 0

Padrão linhas:
    (De 0 até len(linhas)) *

'''
entrada = input().split()
linhas = int(entrada[0])
colunas = int(entrada[1])
num = int(entrada[2])


lista = []

for i in range(linhas):
    linha = input().split()
    linha = [int(i) for i in linha]
    lista.append(linha)

# generate matrix's column
column = []
for i in range(len(lista)):
    precolumn = []
    for f in range(len(lista[i])):
        precolumn.append(lista[f][i])
    column.append(precolumn)


def magica(lista,qnt=1):
    soln = [row[:] for row in lista]
    for x in range(0, len(lista)):
        for j in range(0, len(column[x])):
            #print(x,j)
            soln[j][len(lista)-1-x] = lista[x][j]

    if qnt == 1:
        return soln
    elif qnt == 0:
        return lista
    else:
        return magica(soln,qnt-1)

if num >= 0:
    final = magica(lista,num)
    for i in range(len(final)):
        for j in range(len(final[i])):
            if j == len(final[i])-1:
                print(final[i][j],end="")
            else:
                print(final[i][j], end=" ")
        print()

'''
for i in range(len(column)):
    for f in range(len(lista)-1,-1,-1):
        #moved -->
        #lista[f][i] = lista[f][i]
        print(f,i)


    print()


print("*"*20)
print(lista)




for i in range(len(lista)-1,-1,-1):
    for f in range(len(column[i])):
        #moved -->
        print(f,i)
        
        
        
for f in range(len(lista)):
    for j in range(len(lista[f])):
        print(f,j)
    print()

'''