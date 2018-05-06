pessoas = []
contador = 0
notas = []
while True:
    cod = int(input())
    if cod == 999:
        break
    contador += 1
    nota = float(input())
    notas.append(nota)


    pessoas.append([nota,[cod]])

media = sum(notas) / contador
maiorNota = sorted(pessoas)

print (maiorNota[0][1][0])
print ('%.2f'%media)