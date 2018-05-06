'''
C 0 10 -- saiu (nao muda length)
C 1 10
C 2 10 -- saiu (nao muda length)

posCarros [-1][1] = placa do ultimo
posCarros [-1][0] = id do ultimo


posCarros = [ [0,[placa]], [1,[placa]], [2,[placa]] ]

if posCarros [-1][0] >= posCarros [-2][0] : tira normal
            ||||||||||||||||||||||||||||||||
      if ultimoPos >= verificadoPos: tira normal
      else: ignora e joga no acumulador de espaço vago mas
                            indisponivel

o verificado é menor que o ultimo

if verificadoPos <= ultimoPos: não tira e joga no acumulador

EXCEÇÃO: se o len(posCarros ) == 1 o igual nao se aplica e faz:
lenghtDisponivel = acumulador + lenghtCarro

TESTE:
C 0 10
C 1 10
C 2 10

GANHOS : 0

posCarros = [ [0,[placa]], [1,[placa]], [2,[placa]] ]
s 0
acumulador += length[0] -> +10

GANHOS : 10


posCarros = [ [1,[placa]], [2,[placa]] ]
s 2
acumulador += length[2] -> +10


GANHOS : 20

posCarros = [ [1,[placa]] ] ----> EXCEÇÃO
s 1
lenghtDisponivel = 20 + 10

GANHOS : 30

C 4 20
posCarros = [ [3,[placa]] ]

GANHOS : 40
s 4

c 5 30

GANHOS : 50


sortedID = [ [2,[placa]], [1,[placa]], [0,[placa]] ]
'''
while True:
    parkingInfo = input().split()
    avaibleLength = int(parkingInfo[0])
    nAcctions = int(parkingInfo[1])
    if avaibleLength == -1 and nAcctions == -1: break
    income = 0


    # define before use variables
    parkedCars = {}
    vehiclePosition = []

    count = 0
    countID = 0
    cumulativeLength = 0

    while count < nAcctions:
        count += 1

        vehicleInfo = input().split()
        acction = vehicleInfo[0].lower()
        plaque = int(vehicleInfo[1])

        # if the car is comming in the park
        if acction == "c":

            vehicleLength = int(vehicleInfo[2])

            if avaibleLength > 0 and ((avaibleLength - vehicleLength) >= 0):
                if plaque not in parkedCars:
                    vehiclePosition.append([countID, [plaque]])
                    avaibleLength -= vehicleLength
                    parkedCars[plaque] = vehicleLength
                    income += 10

                    #print(vehiclePosition, "registrado")
                    countID += 1

            else:
                #print(plaque,"n registrado")
                pass

            #print("avaibleLength:", avaibleLength)
            print(vehiclePosition)
        elif acction == "s":
            try:
                #print(vehiclePosition)
                #avaibleLength += parkedCars[plaque]
                lastPos = vehiclePosition[-1][0]

                for i in range(len(vehiclePosition)):
                    if vehiclePosition[i][1][0] == plaque:
                        global removeAfter
                        removeAfter = i
                        verifiedPos = vehiclePosition[i][0]
                        print(verifiedPos, lastPos)
                        if (verifiedPos < lastPos) and len(vehiclePosition) > 1:
                            print("verifiedPos < lastPos")
                            cumulativeLength += parkedCars[plaque]

                        elif verifiedPos == lastPos:
                            if len(vehiclePosition) > 1:
                                avaibleLength += parkedCars[plaque]
                                print("verifiedPos == lastPos and len(vehiclePosition) > 1")
                            elif len(vehiclePosition) == 1:
                                print("len(vehiclePosition) == 1")
                                avaibleLength += cumulativeLength + parkedCars[plaque]



                print("avaibleLength depois:",avaibleLength)

                del parkedCars[plaque]
                del vehiclePosition[removeAfter]


            except KeyError:
                pass

        #print(vehiclePosition)

    print(parkedCars)
    print(income)
    income = 0
    parkedCars = {}