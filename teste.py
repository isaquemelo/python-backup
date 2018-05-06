while True:
    parkingInfo = input().split()
    avaibleLength = int(parkingInfo[0])
    nAcctions = int(parkingInfo[1])
    if avaibleLength == -1 and nAcctions == -1: break
    income = 0


    # define before use variables
    parkedCars = {}
    vehiclePosition = {}

    count = 0
    lastPosition = 0
    while count < nAcctions:
        count += 1

        vehicleInfo = input().split()
        acction = vehicleInfo[0].lower()
        plaque = int(vehicleInfo[1])

        # if the car is comming in the park
        if acction == "c":

            vehicleLength = int(vehicleInfo[2])

            if avaibleLength > 0 and ((avaibleLength - vehicleLength) >= 0):
                lastPosition += 1
                if plaque not in parkedCars:
                    avaibleLength -= vehicleLength
                    parkedCars[plaque] = vehicleLength
                    vehiclePosition[plaque] = lastPosition
                    print(plaque,"with ID:",lastPosition,"\nregistrado")
                    income += 10

            else:
                print(plaque,"n registrado")

            print("avaibleLength:", avaibleLength)

        elif acction == "s":
            try:

                if vehiclePosition[plaque] < lastPosition:
                    print(vehiclePosition[plaque],lastPosition)
                    print("That's right")
                    print("avaibleLength:", avaibleLength)
                else:
                    print(lastPosition, vehiclePosition[plaque])
                    print("avaibleLength:", avaibleLength)
                    avaibleLength += parkedCars[plaque]
                    print("avaibleLength depois:",avaibleLength)

                del vehiclePosition[plaque]
                del parkedCars[plaque]


            except KeyError:
                pass

        #print(vehiclePosition)

    print(parkedCars)
    print(income)
    income = 0
    parkedCars = {}