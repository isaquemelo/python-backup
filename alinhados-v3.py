'''
6 4
7 6
8 8
9 10


p(6,4)
p (9,10)


soma[0] dx
soma[1] dy


ultimo valor (y) - primeiro (y0)
________________________________    =  M inicial        n = 1
ultimo valor (x) - primeiro (x0)


ultimo valor (y) - segundo (y0)
________________________________    =  M secundario     n = 2
ultimo valor (x) - segundo (x0)



'''

numeros = [[6, 4], [7, 6], [9, 10]]
qnt = 3
slopes = []

for i in range(qnt):
    soma = []
    ultimo = qnt - 1
    #print(numeros[i])
    #print(numeros[ultimo])

    for valores1, valores0 in zip(numeros[i], numeros[ultimo]):
        soma.append(valores1 - valores0)
    try:
        slope = soma[1] / soma[0]
    except:
        pass
    slopes.append(slope)
    #print(slope, "\n")

for h in slopes:
    if h != sum(slopes)/qnt:
        iguais = False
    else:
        iguais = True
