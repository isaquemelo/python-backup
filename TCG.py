vida = int(input())
vida1 = vida
vida2 = vida

criaturas1 = []
criaturas2 = []

count = 0

while True:
    if vida1 <= 0 or vida2 <= 0:
        '''
        print("vida1:", vida1)
        print("vida2:", vida2)
        print("Criaturas 1", criaturas1)
        print("Criaturas 2", criaturas2)
        '''
        break
    '''
    print("vida1:",vida1)
    print("vida2:", vida2)
    print("Criaturas 1", criaturas1)
    print("Criaturas 2", criaturas2)
    '''
    # jogador 2
    if count % 2 == 0:
        #print("Jogador 1:")


        jogada = list(input().upper())
        tipo = jogada[0]
        vulnerabilidade_tipo = jogada[1]

        if tipo == 'M':
            forca = int(input())

            if not criaturas2: # sem criaturas - ataque direto
                vida2 -= forca

            elif vulnerabilidade_tipo in criaturas2:
                criaturas2.remove(vulnerabilidade_tipo)

            #print(tipo, vulnerabilidade_tipo, forca)

        elif tipo == 'C':
            criaturas1.append(vulnerabilidade_tipo)
            #print(tipo, vulnerabilidade_tipo, criaturas1)

    # jogador 1
    else:
        #print("Jogador 2:")

        jogada = list(input().upper())
        tipo = jogada[0]
        vulnerabilidade_tipo = jogada[1]

        if tipo == 'M':
            forca = int(input())
            if not criaturas1:
                vida1 -= forca

            elif vulnerabilidade_tipo in criaturas1:
                criaturas1.remove(vulnerabilidade_tipo)

            #print(tipo, vulnerabilidade_tipo, forca )

        elif tipo == 'C':
            criaturas2.append(vulnerabilidade_tipo)
            #print(tipo, vulnerabilidade_tipo,criaturas2)

    count += 1

if vida1 > vida2:
    print("O jogador 1 ganhou!")
else:
    print("O jogador 2 ganhou!")