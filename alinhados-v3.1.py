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
________________________________    =  M inicial = dy/dx     n = 1
ultimo valor (x) - primeiro (x0)


ultimo valor (y) - segundo (y0)
________________________________    =  M secundario     n = 2
ultimo valor (x) - segundo (x0)



'''

qnt = 1
numeros = []
slopes = []
slope = 0
iguais = str("ALINHADOS")

while qnt != 0:
    qnt = int(input("Quantos pontos você gostaria de verificar?"))
    if qnt > 2:
        for f in range(qnt):
            aeb = str(input()).split()
            for i in aeb:
                a = int(aeb[0])
                b = int(aeb[1])
            ab = [a, b]
            numeros.append(ab)

        for i in range(qnt):
            soma = []
            ultimo = qnt - 1

            for valores1, valores0 in zip(numeros[i], numeros[ultimo]):
                soma.append(valores1 - valores0)

            try:
                slope = soma[1] / soma[0]
            except ZeroDivisionError:
                pass

            slopes.append(slope)

        for h in slopes:
            if h != sum(slopes) / qnt:
                iguais = str("NAO_ALINHADOS")
            else:
                iguais = str("ALINHADOS")

        print(iguais)
        del numeros[:]
        del slopes [:]

    else:
        pass

