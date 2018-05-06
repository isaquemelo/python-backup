numero = 1
valores = []
ms = []
while numero != 0:
    numero = int(input("Quantos valores? "))
    if numero == 0:
        pass
    else:
        for i in range(numero):
            x = int(input("x: "))
            y = int(input("y: "))
            valor = [x, y]
            valores.append(valor)

        for f in range(numero):
            soma = []
            for valores0, valores1 in zip(valores[0], valores[-1]):
                soma.append(valores1 - valores0)
                resultado = soma[0] / soma[-1]
                ms.append(resultado)
        print (soma)
        print(ms)

        #soma = [ y - x for x, y in zip(valores[0], valores[-1])]
        #m = soma[-1]/soma[0]
        #try :
        #    print (m)
        #    teste = soma[-1]/soma[1]
        #    if teste != m :
        #        print (teste)
        #        print ("Desalinhado")
        #    else:
        #        print ("Alinhado")
        #except:
        #    pass

