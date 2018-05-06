def processa_lista(lista):
    contador = 0
    for i in range(len(lista)):
        if i <= len(lista) - 2:
            if (lista[i] == "c" and lista[i + 1] == "f") or ((lista[i + 1] == "c" and lista[i] == "f")):
                # print(lista[i],lista[i+1])
                contador += 1
                del lista[i]
                del lista[i]
            elif (lista[i] == "b" and lista[i + 1] == "s") or ((lista[i + 1] == "b" and lista[i] == "s")):
                # print(lista[i], lista[i + 1])
                contador += 1
                del lista[i]
                del lista[i]

    return contador

while True:
    entrada = input().lower()
    if entrada == "z":
        break
    lista = []
    for j in entrada:
        lista.append(j)

    '''
    
    B e S || C e F
    
    
    inicial:
    C F C B S F F S B C C B
    
    C F 
    B S sobra C 
        sobra F e F
    S B
        sobra C C e B 
    
    novo array de sobras:
    C F F C C B
    
    C F
    F C
       sobra C e B
    '''

    contador = 0

    soma = 0
    while True:
        for i in range(len(lista) // 2):
            soma += (processa_lista(lista))
        print(soma)
        break
