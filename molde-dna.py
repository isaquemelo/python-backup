entrada = [0]
t = []
pacientecount = []

while True:
    entrada = input().split()
    if int(entrada[0]) == 9999:
        break
    cod = int(entrada[0])
    dna = [entrada[1]]
    #conta as tininas
    for i in dna:
        count = 0
        for h in i:

            if h == "T":
                count += 1
    pacientecount.append([count,cod])

kzero = []
for k in pacientecount:
    #k[0] = quantidade de tininas
    #k[1] = cod

    kzero.append([k[0],[k[1]]])


finalFilter = sorted(kzero, reverse=True)
print (finalFilter[0][1][0])
