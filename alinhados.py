numero = 1
valores = []
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

        # m = y1 - y0 / x1 - x0
        # valores[0] = (x,y)
        # valores[1] = (x0,y0)
        soma = [ y - x for x, y in zip(valores[0], valores[-1])]
        m = soma[-1]/soma[0]
        try :
            print (m)
            teste = soma[-1]/soma[1]
            if teste != m :
                print (teste)
                print ("Desalinhado")
            else:
                print ("Alinhado")
        except:
            pass

