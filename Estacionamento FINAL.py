while True:
    parkingInfo = input().split()
    avaibleLength = int(parkingInfo[0])
    nAcctions = int(parkingInfo[1])
    if avaibleLength == -1 and nAcctions == -1: break


    income = 0
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

        if acction == "c":
            vehicleLength = int(vehicleInfo[2])

            if avaibleLength > 0 and ((avaibleLength - vehicleLength) >= 0):
                if plaque not in parkedCars:
                    vehiclePosition.append([countID, [plaque]])
                    avaibleLength -= vehicleLength
                    parkedCars[plaque] = vehicleLength
                    income += 10
                    countID += 1

            else:
                pass

        elif acction == "s":
            try:
                lastPos = vehiclePosition[-1][0]

                for i in range(len(vehiclePosition)):
                    if vehiclePosition[i][1][0] == plaque:
                        global removeAfter
                        removeAfter = i
                        verifiedPos = vehiclePosition[i][0]

                        if (verifiedPos < lastPos) and len(vehiclePosition) > 1:
                            cumulativeLength += parkedCars[plaque]

                        elif verifiedPos == lastPos:
                            if len(vehiclePosition) > 1:
                                avaibleLength += parkedCars[plaque]

                            elif len(vehiclePosition) == 1:
                                avaibleLength += cumulativeLength + parkedCars[plaque]



                del parkedCars[plaque]
                del vehiclePosition[removeAfter]


            except:
                pass

    print(income)
    income = 0
    parkedCars = {}