'''
Correnteza = Direita: 0
	Cardume à Esquerda
Correnteza = Esquerda: 1
	Cardume à Direita

'''


'''
x1 y1 = REDE
x2 y2 = REDE
S     = CORRENTE
x3 y3 = PEIXES


1 2 1 5 1 5 3
1 2 1 5 0 5 3


'''


entrada = input().split()

#define variaveis principais e converte-as
rede = [int(entrada[0]),int(entrada[1])]
rede1 = [int(entrada[2]),int(entrada[3])]
corrente = entrada[4]
peixes = [int(entrada[5]),int(entrada[6])]


#cria coordenadas individuais
#peixe
peixeX = peixes[0]
peixeY = peixes[1]
#rede
redeX = rede[0]
redeY = rede[1]
#rede1
rede1X = rede1[0]
rede1Y = rede1[1]

#cria intervalo de trabalho
intervaloY = rede1[1] - rede[1]

#informações
'''
print("\n\npeixeY: ",peixeY)
print("redeY: ",redeY)
print("rede1Y: ",rede1Y,end="\n\n")
print("\n\npeixeX: ",peixeX)
print("redeX: ",redeX)
print("rede1X: ",rede1X,end="\n\n")
'''

#avalia correnteza
if corrente == "1":
    corrente = "esquerda"
elif corrente == "0":
    corrente = "direita"

#verifica se o peixe está no alcance da rede no eixo y
#if peixeY <= rede1Y and peixeY >= redeY:


#lado do peixe:
if peixeX > (redeX or rede1X):
    #cardume à direita
    if corrente == "esquerda":
        pega = True
    else:
        pega = False
elif peixeX < (redeX or rede1X):
    # cardume à esquerda
    if corrente == "direita":
        pega = True
    else:
        pega = False
else:
    # cardume em cima dos pontos
    pega = True

if pega:
    print("S")
else:
    print("N")



'''
1 2 1 5 1 5 3

1 2 1 5 1 1 3

1 2 1 5 0 5 3
'''