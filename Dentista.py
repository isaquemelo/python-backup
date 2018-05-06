qnt = int(input().strip())
agenda = []
for i in range(qnt):
    horario = input().split()
    inicio = int(horario[0])
    fim = int(horario[1])
    agenda.append([inicio,[fim]])




count = 0


def magica(agenda):
    count = 0
    vaga = 1
    ocupado = [agenda[0][0], agenda[0][1][0]]
    #print(ocupado)
    for i in agenda:
        #print(i[0])
        if count != 0:
            if i[0] < ocupado[1]:
                pass
            elif i[0] >= ocupado[1]:
                ocupado = [i[0],i[1][0]]
                vaga += 1
            else:
                vaga += 1
        #print(ocupado)
        count +=1
    return vaga

print(magica(agenda))