qty = int(input("Qual o número de partidas? "))
count = 0

linha1 = []
linha2 = []
linha3 = []


def verifica(listaHorizontal, listaVertical, listaDiagonal):
    def valida(lista):
        o = x = 0
        for i in range(3):
            for f in lista[i]:
                if f == "x":
                    x += 1
                elif f == "o":
                    o += 1
        return [x, o]

    def ganha(lista):
        ganhou = []
        for i in range(len(lista)):
            if (lista[i][0] == lista[i][1] == lista[i][2]):
                if (lista[i][0] and lista[i][1] and lista[i][2]) != "_":
                    ganhou += lista[i][0]

            if len(ganhou) > 1:
                if ganhou[0] == ganhou[-1]:
                    pass
                elif ganhou[0] != ganhou[-1]:
                    return "ILEGAL"

        return ganhou


    validor = valida(listaHorizontal)
    if (validor[0] == validor[-1]-1) or (validor[-1] == validor[0]-1):
        if (validor[0] or validor[-1]) <= 1:
            print("EM_ANDAMENTO")
            return
        pass

    else:
        print ("ILEGAL")
        return

    ganhaH = ganha(listaHorizontal)
    ganhaV = ganha(listaVertical)
    ganhaD = ganha(listaDiagonal)

    if len(ganhaH) >= 1:
        print("\n{} VENCEU".format(ganhaH[0].upper()))
        return

    if len(ganhaV) >= 1:
        print("\n{} VENCEU".format(ganhaV[0]).upper())
        return

    if len(ganhaD) >= 1:
        print("\n{} VENCEU".format(ganhaD[0]).upper())
        return

    print("ILEGAL")
    return

while count < qty:
    count += 1
    for i in range(1,4):
        jogada = input().lower().split()
        if i == 1:
            linha1 += jogada
        elif i == 2:
            linha2 += jogada
        elif i == 3:
            linha3 += jogada

    horizontal = [linha1, linha2, linha3]
    vertical = [[linha1[0], linha2[0], linha3[0]], [linha1[1], linha2[1], linha3[1]], [linha1[2], linha2[2], linha3[2]]]
    diagonal = [[linha1[0], linha2[1], linha3[2]], [linha1[2], linha2[1], linha3[0]]]

    verifica(horizontal,vertical,diagonal)

    del linha1[:], linha2[:], linha3[:]
